import pandas as pd

from measurements.Direction import Direction
from measurements.Measurement import Measurement
from Point import Point


class Station:

    def __init__(self, station_point: Point):
        self.station_point = station_point
        self._measurements = []
        self.dz = None

    def __iter__(self):
        return iter(self._measurements)

    def get_a_sub_df_for_station(self):
        station_coefficient_df = pd.DataFrame()
        for measure in self:
            measure_df = measure.get_coefficients_df()
            station_coefficient_df = pd.concat([station_coefficient_df, measure_df]).fillna(0)
        return station_coefficient_df

    def get_p_sub_df_for_station(self):
        station_p_df = pd.DataFrame()
        for measure in self:
            p_df = pd.DataFrame([{"p": measure.p}], index=[measure.get_index()])
            station_p_df = pd.concat([station_p_df, p_df])
        return station_p_df

    def get_direction_coefficients_and_p_for_station(self):
        dir_m = [measurement for measurement in self if isinstance(measurement, Direction)]
        st_df = pd.DataFrame()
        sum_p = 0
        for dir in dir_m:
            c = dir.get_coefficients_df()
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
        # print(dz_equivalent)
        return dz_equivalent, p_df
        # print(sum)
        # st_df = st_df._append(sum, ignore_index=False)
        # # print(sum.to_numpy())
        # # print(list(st_df))
        # # st_df = pd.DataFrame(list(sum.to_numpy()), columns=["q1", "q2"])
        # print(st_df)

    def add_measurement(self, measurement: Measurement):
        if self.station_point == measurement.start_point:
            self._measurements.append(measurement)
        else:
            raise ValueError(f"Измерение не относится к станции {self.station_point} ({measurement})")
