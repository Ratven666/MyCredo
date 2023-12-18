from math import sin, cos

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

from measurements.directions.Azimuth import Azimuth
from measurements.composite_measurments.CompositeMeasurementsABC import CompositeMeasurementsABC
from measurements.directions.Direction import Direction
from measurements.distances.HorizontalDistance import HorizontalDistance
from measurements.MeasurementABC import MeasurementABC
from measurements.composite_measurments.TotalStationDirections import TotalStationDirection3D


class ProjectMPLPlotter:

    def __init__(self, scale):
        self.project = None
        self.scale = scale
        self.fig, self.ax = plt.subplots()

    def _plot_points(self):
        font_size = self.scale / 2.5
        offset = self.scale / 10
        for base_point in self.project.points["base_points"].values():
            self.ax.scatter(base_point.y, base_point.x, c="red", s=self.scale)
            self.ax.text(base_point.y + offset,
                         base_point.x + offset,
                         base_point.point_name,
                         c="red", fontsize=font_size)
            self.ax.text(base_point.y + offset,
                         base_point.x - offset * 2,
                         f"z={base_point.z}",
                         c="black", fontsize=font_size / 1.2)
        for evaluated_point in self.project.points["evaluated_points"].values():
            self.ax.scatter(evaluated_point.y, evaluated_point.x, c="blue", s=self.scale)
            self.ax.text(evaluated_point.y + offset,
                         evaluated_point.x + offset,
                         evaluated_point.point_name,
                         c="blue", fontsize=font_size)
            self.ax.text(evaluated_point.y + offset,
                         evaluated_point.x - offset * 2,
                         f"z={evaluated_point.z}",
                         c="black", fontsize=font_size / 1.2)

    def _plot_stations(self):
        for station in self.project.stations.values():
            for measurement in station._measurements:
                self._plot_measurement(measurement)

    def _plot_measurement(self, measurement: MeasurementABC):
        if isinstance(measurement, TotalStationDirection3D):
            for item in measurement:
                self._plot_measurement(measurement=item)
        if isinstance(measurement, HorizontalDistance):
            self._plot_distance(measurement)
        if isinstance(measurement, Direction):
            self._plot_direction(measurement)
        if isinstance(measurement, Azimuth):
            self._plot_azimuth(measurement)
        if isinstance(measurement, CompositeMeasurementsABC):
            for measure in measurement:
                self._plot_measurement(measure)

    def _plot_distance(self, distance: HorizontalDistance):
        self.ax.plot([distance.start_point.y, distance.end_point.y],
                     [distance.start_point.x, distance.end_point.x],
                     c="blue")

    def _plot_direction(self, direction: Direction):
        x = direction.start_point.y
        y = direction.start_point.x
        dx = sin(direction.azimuth) * direction.horizontal_distance / 4
        dy = cos(direction.azimuth) * direction.horizontal_distance / 4
        self.ax.arrow(x=x, y=y, dx=dx, dy=dy,
                      width=0.8,
                      facecolor="red",
                      edgecolor="none",
                      alpha=0.8,
                      )
        self.ax.plot([direction.start_point.y, direction.end_point.y],
                     [direction.start_point.x, direction.end_point.x],
                     c="red",
                     linestyle=":")

    def _plot_azimuth(self, azimuth: Azimuth):
        x = azimuth.start_point.y
        y = azimuth.start_point.x
        dx1 = sin(azimuth.azimuth) * azimuth.horizontal_distance / 10
        dy1 = cos(azimuth.azimuth) * azimuth.horizontal_distance / 10
        dx2 = sin(azimuth.azimuth) * azimuth.horizontal_distance / 8
        dy2 = cos(azimuth.azimuth) * azimuth.horizontal_distance / 8
        self.ax.arrow(x=x, y=y, dx=dx1, dy=dy1,
                      width=0.8,
                      facecolor="green",
                      edgecolor="none",
                      alpha=0.7,
                      )
        self.ax.arrow(x=x, y=y, dx=dx2, dy=dy2,
                      width=0.8,
                      facecolor="green",
                      edgecolor="none",
                      alpha=0.7,
                      )
        self.ax.plot([azimuth.start_point.y, azimuth.end_point.y],
                     [azimuth.start_point.x, azimuth.end_point.x],
                     c="green",
                     linestyle="--")

    def _plot_mse_ellipses(self):
        for point in self.project.points["evaluated_points"].values():
            if point.mse_data is None:
                continue
            self.ax.add_artist(Ellipse(xy=[point.y, point.x],
                                       width=point.mse_data["a"] * 500,
                                       height=point.mse_data["b"] * 500,
                                       angle=point.mse_data["theta"],
                                       fill=False,
                                       ))

    def _set_plot_limits(self):
        x, y = [], []
        for point in self.project.points["all_points"].values():
            x.append(point.x)
            y.append(point.y)
        x_min, x_max = min(x), max(x)
        y_min, y_max = min(y), max(y)
        limits = [x_max - x_min,
                  y_max - y_min]
        length = max(limits) / 2 + 20
        y_lim = [(x_min + x_max / 2) - length, (x_min + x_max / 2) + length]
        x_lim = [(y_min + y_max / 2) - length, (y_min + y_max / 2) + length]
        self.ax.set_xlim(*x_lim)
        self.ax.set_ylim(*y_lim)

    def plot(self, project):
        self.project = project
        self._plot_points()
        self._plot_stations()
        self._plot_mse_ellipses()
        self._set_plot_limits()
        plt.show()
