from abc import ABC

from base.Point import Point
from accuracy_classes.AccuracyClass import AccuracyClass
from measurements.MeasurementABC import MeasurementABC


class DistanceABC(MeasurementABC, ABC):

    def __init__(self, start_point: Point, end_point: Point, mse_class: AccuracyClass,
                 is_distance_measuring_tape=False):
        super().__init__(start_point=start_point, end_point=end_point, mse_class=mse_class)
        self.is_distance_measuring_tape = is_distance_measuring_tape
        self._init_measure_mse()

    def _init_measure_mse(self):
        if self.is_distance_measuring_tape is False:
            self.mse = (self.mse_class.distance_mse_a +
                        self.mse_class.distance_mse_b * self.slope_distance / 1_000_000)
        else:
            self.mse = self.mse_class.relative_distance_mse * self.slope_distance
