from MeasurementABC import MeasurementABC
from Point import Point
from accuracy_classes.AccuracyClass import AccuracyClass


class Elevation(MeasurementABC):

    def __init__(self, start_point: Point, end_point: Point, mse_class: AccuracyClass):
        super().__init__(start_point=start_point, end_point=end_point, mse_class=mse_class)
        self._init_measure_mse()

    def _init_measure_mse(self):
        self.mse = self.mse_class.elevation_mse
