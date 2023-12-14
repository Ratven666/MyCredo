import numpy as np
import pandas as pd

from CONFIG import MU_0


class Calculator:

    point_indexes = {}

    def __init__(self, project):
        self.project = project
        self.a_df = None
        self.p_df = None



    def calculate(self):
        self.get_point_order()
        # self.create_a_matrix_structure()
        self.calk_matrices()
        # self.a_df.fillna(0)
        # print(self.a_df)
        # print(self.p_df)
        A, P = self.calc_np_arrays()
        N = A.T @ P @ A
        # print(N)
        Q = np.linalg.inv(N)
        # print(Q)
        K = (MU_0 ** 2) * Q
        print(np.sqrt(np.diagonal(K)))
        values_order = list(self.a_df)
        df = pd.DataFrame(K, columns=values_order, index=values_order)
        # print(df)

    def get_point_order(self):
        count = 0
        for point in self.project.points["evaluated_points"].values():
            self.point_indexes[point.point_name] = count
            count += 1

    def create_a_matrix_structure(self):
        evaluated_points_coord_lst = []
        for point in self.project.points["evaluated_points"].values():
            evaluated_points_coord_lst.append(f"{point.point_name}_x")
            evaluated_points_coord_lst.append(f"{point.point_name}_y")
            evaluated_points_coord_lst.append(f"{point.point_name}_z")
        self.a_df = pd.DataFrame(columns=evaluated_points_coord_lst)

    def calk_matrices(self):
        for station in self.project.stations.values():
            station_a_coefficient_df, station_p_df = station.get_a_and_p_sub_df_for_station()
            # station_df = station.get_a_sub_df_for_station()
            self.a_df = pd.concat([self.a_df, station_a_coefficient_df]).fillna(0)
            self.p_df = pd.concat([self.p_df, station_p_df]).fillna(0)
            # self.a_df = pd.concat([self.a_df, station_df]).fillna(0)
            # self.p_df = pd.concat([self.p_df, station.get_p_sub_df_for_station()]).fillna(0)

            dz_equivalent, p = station.get_direction_coefficients_and_p_for_station()
            self.a_df = self.a_df._append(dz_equivalent, ignore_index=False).fillna(0)
            self.p_df = pd.concat([self.p_df, p]).fillna(0)

    def calc_np_arrays(self):
        A = self.a_df.to_numpy()
        P = self.p_df.to_numpy()
        P = np.diag(P.T[0])
        return A, P

