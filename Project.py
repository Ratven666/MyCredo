from Calculator import Calculator
from Point import Point
from Station import Station
from measurements.CompositeMeasurementsABC import CompositeMeasurementsABC
from measurements.MeasurementABC import MeasurementABC
from plotters.ProjectMPLPlotter import ProjectMPLPlotter


class Project:

    points = {"all_points": {},
                "base_points": {},
                "evaluated_points": {},
              }

    stations = {}

    def __init__(self, project_name):
        self.project_name = project_name
        self._calculator = None

    @property
    def k_df(self):
        if self._calculator is None:
            self.calculate()
        return self._calculator.k_df

    @property
    def mse_df(self):
        if self._calculator is None:
            self.calculate()
        return self._calculator.get_mse_df()

    def calculate(self, calculator=Calculator):
        self._calculator = calculator(project=self)
        self._calculator.calculate()

    def add_point(self, point: Point):
        self.points["all_points"][point.point_name] = point
        if point.is_base_point:
            self.points["base_points"][point.point_name] = point
        else:
            self.points["evaluated_points"][point.point_name] = point

    def add_points(self, points):
        for point in points:
            self.add_point(point)

    def add_station(self, station: Station):
        self.stations[station.station_point.point_name] = station

    def add_measurement(self, measurement: [MeasurementABC, CompositeMeasurementsABC]):
        base_point = measurement.start_point
        if base_point.point_name in self.stations:
            self.stations[base_point.point_name].add_measurement(measurement)
        else:
            station = Station(station_point=base_point)
            station.add_measurement(measurement=measurement)
            self.add_station(station=station)
        self.add_point(measurement.start_point)
        self.add_point(measurement.end_point)

    def plot(self, scale=10, plotter=ProjectMPLPlotter):
        plotter = plotter()
        plotter.scale = scale
        plotter.plot(self)
