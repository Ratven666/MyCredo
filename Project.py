from Calculator import Calculator
from Point import Point
from Station import Station
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

    def calculate(self, calculator=Calculator):
        self._calculator = calculator(self)
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

    def plot(self, scale=10, plotter=ProjectMPLPlotter):
        plotter = plotter()
        plotter.scale = scale
        plotter.plot(self)


