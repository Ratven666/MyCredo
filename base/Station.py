import pandas as pd

from measurements.AbstractMeasureABC import AbstractMeasureABC
from measurements.MeasuredPoint import MeasuredPoint
from measurements.composite_measurments.CompositeMeasurementsABC import CompositeMeasurementsABC
from measurements.directions.Direction import Direction
from measurements.MeasurementABC import MeasurementABC
from base.Point import Point


class Station:

    def __init__(self, station_point: Point):
        self.station_point = station_point
        self._measurements = []

    def __iter__(self):
        return iter(self._measurements)

    def get_a_and_p_sub_df_for_station(self):
        station_a_coefficient_df = pd.DataFrame()
        station_p_df = pd.DataFrame()
        for measure in self:
            station_a_coefficient_df = pd.concat([station_a_coefficient_df, measure.get_a_coefficients_df()]).fillna(0)
            station_p_df = pd.concat([station_p_df, measure.get_p_df()]).fillna(0)
        return station_a_coefficient_df, station_p_df

    def get_direction_coefficients_and_p_for_station(self):
        dir_m = []
        for measurement in self:
            if isinstance(measurement, Direction):
                dir_m.append(measurement)
            if isinstance(measurement, CompositeMeasurementsABC):
                for measure in measurement:
                    if isinstance(measure, Direction):
                        dir_m.append(measure)
        st_df = pd.DataFrame()
        sum_p = 0
        for direction in dir_m:
            c = direction.get_a_coefficients_df()
            c = c.mul(direction.p)
            st_df = pd.concat([st_df, c]).fillna(0)
            sum_p += direction.p
        dz_equivalent = st_df.sum()
        dz_equivalent.name = f"{self.station_point.point_name}_dz"
        try:
            p = -1 / sum_p
        except ZeroDivisionError:
            p = 0
        p_df = pd.DataFrame([{f"{self.station_point.point_name}_dz": p}], index=[f"{self.station_point.point_name}_dz"])
        return dz_equivalent, p_df

    def add_measurement(self, measurement: AbstractMeasureABC):
        if isinstance(measurement, MeasuredPoint) and measurement.point == self.station_point:
            self._measurements.append(measurement)
            return
        if self.station_point == measurement.start_point:
            self._measurements.append(measurement)
        else:
            raise ValueError(f"Измерение не относится к станции {self.station_point} ({measurement})")
