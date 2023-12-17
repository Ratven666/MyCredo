from base.Point import Point
from accuracy_classes.AccuracyClass import AccuracyClass
from measurements.directions.Azimuth import Azimuth
from measurements.composite_measurments.CompositeMeasurementsABC import CompositeMeasurementsABC
from measurements.distances.SlopeDistance import SlopeDistance
from measurements.directions.ZenithAngle import ZenithAngle


class GNSSVector(CompositeMeasurementsABC):

    def __init__(self, start_point: Point, end_point: Point, mse_class: AccuracyClass):
        super().__init__(start_point=start_point, end_point=end_point, mse_class=mse_class)
        self._init_measures([SlopeDistance, Azimuth, ZenithAngle])