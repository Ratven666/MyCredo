from Point import Point
from accuracy_classes.AccuracyClass import AccuracyClass
from measurements.CompositeMeasurementsABC import CompositeMeasurementsABC
from measurements.Direction import Direction
from measurements.HorizontalDistance import HorizontalDistance
from measurements.SlopeDistance import SlopeDistance
from measurements.ZenithAngle import ZenithAngle


class TotalStationDirection3D(CompositeMeasurementsABC):

    def __init__(self, start_point: Point, end_point: Point, mse_class: AccuracyClass):
        super().__init__(start_point=start_point, end_point=end_point, mse_class=mse_class)
        self._init_measures([SlopeDistance, Direction, ZenithAngle])


class TotalStationDirection2D(CompositeMeasurementsABC):

    def __init__(self, start_point: Point, end_point: Point, mse_class: AccuracyClass):
        super().__init__(start_point=start_point, end_point=end_point, mse_class=mse_class)
        self._init_measures([HorizontalDistance, Direction])
