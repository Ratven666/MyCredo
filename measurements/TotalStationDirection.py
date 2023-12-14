import pandas as pd

from CONFIG import MU_0
from Point import Point
from measurements.Direction import Direction
from measurements.Measurement import Measurement
from measurements.SlopeDistance import SlopeDistance
from measurements.ZenithAngle import ZenithAngle


class TotalStationDirection(Measurement):

    def __init__(self, start_point: Point, end_point: Point, mse=0.05):
        super().__init__(start_point=start_point, end_point=end_point, mse=mse)
        self.st_slope_distance = SlopeDistance(start_point=start_point, end_point=end_point)
        self.st_direction = Direction(start_point=start_point, end_point=end_point)
        self.st_zenith = ZenithAngle(start_point=start_point, end_point=end_point)

    def __iter__(self):
        return iter([self.st_slope_distance,
                     self.st_direction,
                     self.st_zenith])

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



        if self.mse == 0:
            return float("inf")
        return (MU_0 ** 2) / (self.mse ** 2)


