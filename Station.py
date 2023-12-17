import pandas as pd

from measurements.CompositeMeasurementsABC import CompositeMeasurementsABC
from measurements.Direction import Direction
from measurements.MeasurementABC import MeasurementABC
from Point import Point


class Station:

    def __init__(self, station_point: Point):
        self.station_point = station_point
        self._measurements = []
        self.dz = None

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
        for dir in dir_m:
            c = dir.get_a_coefficients_df()
            c = c.mul(dir.p)
            st_df = pd.concat([st_df, c]).fillna(0)
            sum_p += dir.p
        dz_equivalent = st_df.sum()
        dz_equivalent.name = f"{self.station_point.point_name}_dz"
        try:
            p = -1 / sum_p
        except ZeroDivisionError:
            p = 0
        p_df = pd.DataFrame([{"p": p}], index=[f"{self.station_point.point_name}_dz"])
        return dz_equivalent, p_df

    def add_measurement(self, measurement: MeasurementABC):
        if self.station_point == measurement.start_point:
            self._measurements.append(measurement)
        else:
            raise ValueError(f"Измерение не относится к станции {self.station_point} ({measurement})")
