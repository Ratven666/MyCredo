import pandas as pd

from CONFIG import MU_0
from base.Point import Point
from measurements.AbstractMeasureABC import AbstractMeasureABC


class MeasuredPoint(AbstractMeasureABC):

    def __init__(self, measured_point: Point,
                 m_x: float,
                 m_y: float,
                 m_z: float,
                 # covariance_matrix=None,
                 ):
        self.point = measured_point
        self.mse_dist = {
            "x": 1e-6 if m_x == 0 else m_x,
            "y": 1e-6 if m_y == 0 else m_y,
            "z": 1e-6 if m_z == 0 else m_z,
        }
        # self.K = covariance_matrix
        self.p_df = None
        self.__init_weights()

    def get_index(self, index_suffice):
        return f"{self.__class__.__name__}_{self.point.point_name}_{index_suffice}"

    def get_a_coefficients_df(self):
        coefficient_dict = pd.DataFrame({f"{self.point.point_name}_x": [1, 0, 0],
                                         f"{self.point.point_name}_y": [0, 1, 0],
                                         f"{self.point.point_name}_z": [0, 0, 1]},
                                        index=[self.get_index("x"), self.get_index("y"), self.get_index("z")])
        return coefficient_dict

    def get_p_df(self):
        return self.p_df

    def __init_weights(self):
        for idx, mse in self.mse_dist.items():
            if mse is None:
                raise ValueError(f"Не указаны СКП m_{idx} для измеренной точки \"{self.point.point_name}\"")
            p = (MU_0 ** 2) / (mse ** 2)
            idx_df = pd.DataFrame({self.get_index(idx): p}, index=[self.get_index(idx)])
            self.p_df = pd.concat([self.p_df, idx_df]).fillna(0)

    def __str__(self):
        return (f"{self.__class__.__name__}(measured_point={self.point},"
                f"m_x={self.mse_dist["x"]}, m_y={self.mse_dist["y"]}, m_z={self.mse_dist["z"]})")


if __name__ == "__main__":
    m_point = MeasuredPoint(measured_point=Point(point_name="m_p1",
                                                 x=0,
                                                 y=0,
                                                 z=0,
                                                 is_base_point=False),
                            m_x=1, m_y=1, m_z=2)
    print(m_point)
    print(m_point.p_df)
