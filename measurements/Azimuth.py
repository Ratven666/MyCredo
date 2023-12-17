import math

import pandas as pd

from Point import Point
from accuracy_classes.AccuracyClass import AccuracyClass
from measurements.MeasurementABC import MeasurementABC


class Azimuth(MeasurementABC):

    def __init__(self, start_point: Point, end_point: Point, mse_class: AccuracyClass):
        super().__init__(start_point=start_point, end_point=end_point, mse_class=mse_class)
        self._init_measure_mse()

    def _init_measure_mse(self):
        self.mse = self.mse_class.azimuth_mse

    def get_a_coefficients_df(self):
        coefficient_dict = {}
        if self.start_point.is_base_point is False:
            coefficient_dict[f"{self.start_point.point_name}_x"] = math.sin(self.azimuth) / self.horizontal_distance
            coefficient_dict[f"{self.start_point.point_name}_y"] = -math.cos(self.azimuth) / self.horizontal_distance
        if self.end_point.is_base_point is False:
            coefficient_dict[f"{self.end_point.point_name}_x"] = -math.sin(self.azimuth) / self.horizontal_distance
            coefficient_dict[f"{self.end_point.point_name}_y"] = math.cos(self.azimuth) / self.horizontal_distance
        coefficient_dict = pd.DataFrame([coefficient_dict], index=[self.get_index()])
        return coefficient_dict
