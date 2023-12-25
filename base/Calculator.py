import math

import numpy as np
import pandas as pd

from CONFIG import MU_0


class Calculator:

    def __init__(self, project):
        self.project = project
        self.a_df = None
        self.p_df = None
        self.k_df = None
        self.mse_df = None

    def calculate(self):
        self.calk_matrices()
        K = self.calculate_covariance_matrix()
        values_order = list(self.a_df)
        self.k_df = pd.DataFrame(K, columns=values_order, index=values_order)
        self._calk_points_mse_ellipses()

    def _calk_points_mse_ellipses(self):
        for point in self.project.points["evaluated_points"].values():
            p_np = self.k_df[[f"{point.point_name}_x",
                              f"{point.point_name}_y"]].loc[[f"{point.point_name}_x",
                                                             f"{point.point_name}_y"]].to_numpy()
            theta = math.degrees(math.atan2((2 * p_np[0][1]), (p_np[0][1] - p_np[1][1])) / 2)
            theta = theta + 360 if theta < 0 else theta
            q = ((p_np[0][0] - p_np[1][1]) ** 2 + 4 * p_np[1][0] ** 2) ** 0.5
            a = ((p_np[0][0] + p_np[1][1] + q) / 2) ** 0.5
            b = ((p_np[0][0] + p_np[1][1] - q) / 2) ** 0.5
            try:
                m_z = self.k_df.loc[f"{point.point_name}_z"][f"{point.point_name}_z"] ** 0.5
            except KeyError:
                m_z = None
            point.mse_data = {"M": (p_np[0][0] + p_np[1][1]) ** 0.5,
                              "m_x": p_np[0][0] ** 0.5,
                              "m_y": p_np[1][1] ** 0.5,
                              "m_z": m_z,
                              "theta": theta,
                              "a": a,
                              "b": b}

    @property
    def points_mse_df(self):
        if self.mse_df is None:
            mse_dict = {}
            for point in self.project.points["evaluated_points"].values():
                mse_dict[point.point_name] = point.mse_data
            self.mse_df = pd.DataFrame(mse_dict)
        return self.mse_df

    def calculate_covariance_matrix(self):
        A, P = self.calc_np_arrays()
        N = A.T @ P @ A
        Q = np.linalg.inv(N)
        K = (MU_0 ** 2) * Q
        return K

    def calk_matrices(self):
        for station in self.project.stations.values():
            station_a_coefficient_df, station_p_df = station.get_a_and_p_sub_df_for_station()
            self.a_df = pd.concat([self.a_df, station_a_coefficient_df]).fillna(0)
            self.p_df = pd.concat([self.p_df, station_p_df]).fillna(0)

            dz_equivalent, p = station.get_direction_coefficients_and_p_for_station()
            self.a_df = self.a_df._append(dz_equivalent, ignore_index=False).fillna(0)
            self.p_df = pd.concat([self.p_df, p]).fillna(0)

    def calc_np_arrays(self):
        A = self.a_df.to_numpy()
        P = self.p_df.to_numpy()
        return A, P
