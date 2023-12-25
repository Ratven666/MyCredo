from abc import ABC, abstractmethod


class AbstractMeasureABC(ABC):

    @abstractmethod
    def get_a_coefficients_df(self):
        pass

    @abstractmethod
    def get_p_df(self):
        pass
