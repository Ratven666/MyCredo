import math

import pandas as pd

from Point import Point
from accuracy_classes.AccuracyClass import AccuracyClass
from measurements.Measurement import Measurement


class SlopeDistance(Measurement):

    def __init__(self, start_point: Point, end_point: Point, mse_class: AccuracyClass):
        super().__init__(start_point=start_point, end_point=end_point, mse_class=mse_class)
        self._init_measure_mse()

    def _init_measure_mse(self):
        self.mse = self.mse_class.distance_mse

    def get_a_coefficients_df(self):
        coefficient_dict = {}
        if self.start_point.is_base_point is False:
            coefficient_dict[f"{self.start_point.point_name}_x"] = -math.cos(self.azimuth)
            coefficient_dict[f"{self.start_point.point_name}_y"] = -math.sin(self.azimuth)
            coefficient_dict[f"{self.start_point.point_name}_z"] = -self.elevation / self.slope_distance
        if self.end_point.is_base_point is False:
            coefficient_dict[f"{self.end_point.point_name}_x"] = math.cos(self.azimuth)
            coefficient_dict[f"{self.end_point.point_name}_y"] = math.sin(self.azimuth)
            coefficient_dict[f"{self.end_point.point_name}_z"] = self.elevation / self.slope_distance
        coefficient_dict = pd.DataFrame([coefficient_dict], index=[self.get_index()])
        return coefficient_dict


if __name__ == "__main__":
    p1 = Point(point_name="p1", x=10, y=10, z=0, is_base_point=True)
    p2 = Point(point_name="p2", x=20, y=10, z=-10, is_base_point=False)

    dist = SlopeDistance(start_point=p1, end_point=p2, mse=0)
    d_lst = [dist, dist]
    print(d_lst)
    print(dist)

    print(dist.horizontal_distance)
    print((dist.azimuth * 180 / math.pi))
    print((dist.zenith * 180 / math.pi))
