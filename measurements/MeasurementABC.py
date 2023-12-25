from abc import ABC, abstractmethod
from math import atan2

import pandas as pd

from CONFIG import MU_0
from base.Point import Point
from accuracy_classes.AccuracyClass import AccuracyClass
from measurements.AbstractMeasureABC import AbstractMeasureABC


class MeasurementABC(AbstractMeasureABC):

    def __init__(self, start_point: Point, end_point: Point, mse_class: AccuracyClass):
        self.start_point = start_point
        self.end_point = end_point
        self.mse_class = mse_class
        self.mse = None

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
                f"end_point={repr(self.end_point)}, mse_class={self.mse_class})")

    def __str__(self):
        return (f"{self.__class__.__name__}(start_point={self.start_point}, "
                f"end_point={self.end_point}, mse_class={self.mse_class})")

    @abstractmethod
    def get_a_coefficients_df(self):
        pass

    @abstractmethod
    def _init_measure_mse(self):
        pass

    def get_p_df(self):
        p_df = pd.DataFrame([{self.get_index(): self.p}], index=[self.get_index()])
        return p_df
