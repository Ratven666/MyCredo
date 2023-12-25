from abc import ABC

import pandas as pd

from base.Point import Point
from accuracy_classes.AccuracyClass import AccuracyClass
from measurements.AbstractMeasureABC import AbstractMeasureABC


class CompositeMeasurementsABC(AbstractMeasureABC):

    def __init__(self, start_point: Point, end_point: Point, mse_class: AccuracyClass):
        self.start_point = start_point
        self.end_point = end_point
        self.mse_class = mse_class
        self.measures = []

    def _init_measures(self, measures_class_list: list):
        for measure_class in measures_class_list:
            self.measures.append(measure_class(self.start_point, self.end_point, self.mse_class))

    def __iter__(self):
        return iter(self.measures)

    def get_a_coefficients_df(self):
        df = pd.DataFrame()
        for item in self:
            item_df = item.get_a_coefficients_df()
            df = pd.concat([df, item_df])
        return df

    @property
    def p(self):
        p = []
        for item in self:
            p.append(item.p)
        return p

    def get_p_df(self):
        p_df = pd.DataFrame()
        for item in self:
            p_df = pd.concat([p_df, item.get_p_df()])
        return p_df
