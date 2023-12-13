from Measurement import Measurement
from Point import Point


class Elevation(Measurement):

    def __init__(self, start_point: Point, end_point: Point, mse):
        super().__init__(start_point=start_point, end_point=end_point, mse=mse)
