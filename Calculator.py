import numpy as np
import pandas as pd

from CONFIG import MU_0


class Calculator:

    def __init__(self, project):
        self.project = project
        self.a_df = None
        self.p_df = None
        self.k_df = None

    def calculate(self):
        self.calk_matrices()
        K = self.calculate_covariance_matrix()
        print(np.sqrt(np.diagonal(K)))
        values_order = list(self.a_df)
        self.k_df = pd.DataFrame(K, columns=values_order, index=values_order)

    def get_mse_df(self):
        K = self.calculate_covariance_matrix()
        values_order = list(self.a_df)
        variance = np.sqrt(np.diagonal(K))
        return pd.Series(variance, index=values_order, name="mse")

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
        P = np.diag(P.T[0])
        return A, P

