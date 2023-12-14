import math

import pandas as pd

from Point import Point
from measurements.Measurement import Measurement


class ZenithAngle(Measurement):

    def __init__(self, start_point: Point, end_point: Point, mse=0.05):
        super().__init__(start_point=start_point, end_point=end_point, mse=mse)

    def get_a_coefficients_df(self):
        hor_dist = self.horizontal_distance
        h = self.elevation
        coefficient_dict = {}
        if self.start_point.is_base_point is False:
            coefficient_dict[f"{self.start_point.point_name}_x"] = ((h * math.cos(self.azimuth)) /
                                                                    (h ** 2 + hor_dist ** 2)) * -1
            coefficient_dict[f"{self.start_point.point_name}_y"] = ((h * math.sin(self.azimuth)) /
                                                                    (h ** 2 + hor_dist ** 2)) * -1
            coefficient_dict[f"{self.start_point.point_name}_z"] = (hor_dist / (hor_dist ** 2 + h ** 2))

        if self.end_point.is_base_point is False:
            coefficient_dict[f"{self.end_point.point_name}_x"] = ((h * math.cos(self.azimuth)) /
                                                                  (h ** 2 + hor_dist ** 2))
            coefficient_dict[f"{self.end_point.point_name}_y"] = ((h * math.sin(self.azimuth)) /
                                                                  (h ** 2 + hor_dist ** 2))
            coefficient_dict[f"{self.end_point.point_name}_z"] = (hor_dist / (hor_dist ** 2 + h ** 2)) * -1
        coefficient_dict = pd.DataFrame([coefficient_dict], index=[self.get_index()])
        return coefficient_dict
