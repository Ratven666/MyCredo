from abc import ABC, abstractmethod
from math import atan2

import pandas as pd

from CONFIG import MU_0
from Point import Point


class Measurement(ABC):

    def __init__(self, start_point: Point, end_point: Point, mse):
        self.start_point = start_point
        self.end_point = end_point
        self.mse = mse

    @property
    def p(self):
        if self.mse == 0:
            return float("inf")
        return (MU_0 ** 2) / (self.mse ** 2)

    @property
    def horizontal_distance(self):
        return ((self.end_point.x - self.start_point.x) ** 2 +
                (self.end_point.y - self.start_point.y) ** 2) ** 0.5

    @property
    def slope_distance(self):
        return ((self.end_point.x - self.start_point.x) ** 2 +
                (self.end_point.y - self.start_point.y) ** 2 +
                (self.end_point.z - self.start_point.z) ** 2) ** 0.5

    @property
    def azimuth(self):
        return atan2(self.end_point.y - self.start_point.y,
                     self.end_point.x - self.start_point.x)

    @property
    def zenith(self):
        return atan2(self.horizontal_distance, self.elevation)

    @property
    def elevation(self):
        return self.end_point.z - self.start_point.z

    def get_index(self):
        return f"{self.__class__.__name__}_{self.start_point.point_name}-{self.end_point.point_name}"

    def __repr__(self):
        return (f"{self.__class__.__name__}(start_point={repr(self.start_point)}, "
                f"end_point={repr(self.end_point)}, mse={self.mse})")

    def __str__(self):
        return (f"{self.__class__.__name__}(start_point={self.start_point}, "
                f"end_point={self.end_point}, mse={self.mse})")

    @abstractmethod
    def get_a_coefficients_df(self):
        pass

    def get_p_df(self):
        p_df = pd.DataFrame([{"p": self.p}], index=[self.get_index()])
        return p_df

