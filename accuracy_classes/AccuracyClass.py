from dataclasses import dataclass


@dataclass
class AccuracyClass:
    angle_mse: float = None
    direction_mse: float = None
    zenith_mse: float = None
    azimuth_mse: float = None
    distance_mse: float = None
    relative_distance_mse: int = None
    elevation_mse: float = None

    def __post_init__(self):
        if self.angle_mse is not None and self.direction_mse is None:
            self.angle_mse /= 206265
            self.direction_mse = self.angle_mse / 2 ** 0.5
        elif self.direction_mse is not None and self.angle_mse is None:
            self.direction_mse /= 206265
            self.angle_mse = self.direction_mse * 2 ** 0.5
        elif self.angle_mse is not None and self.direction_mse is not None:
            self.angle_mse /= 206265
            self.direction_mse /= 206265
        if self.zenith_mse is None:
            self.zenith_mse = self.direction_mse
        else:
            self.zenith_mse /= 206265
        if self.azimuth_mse is not None:
            self.azimuth_mse /= 206265

    def __repr__(self):
        return (f"AccuracyClass(angle_mse={round(self.angle_mse * 206265, 1) if self.angle_mse is not None else None}, "
                f"direction_mse={round(self.direction_mse * 206265, 1) if self.angle_mse is not None else None}, "
                f"zenith_mse={round(self.zenith_mse * 206265, 1) if self.angle_mse is not None else None}, "
                f"azimuth_mse={round(self.azimuth_mse * 206265, 1) if self.angle_mse is not None else None}, "
                f"distance_mse={self.distance_mse}, "
                f"relative_distance_mse=1/{self.relative_distance_mse}, "
                f"elevation_mse={self.elevation_mse})")


if __name__ == "__main__":
    first_class = AccuracyClass(angle_mse=30,
                                direction_mse=14.1,
                                azimuth_mse=30,
                                distance_mse=0.01,
                                zenith_mse=5,
                                )
    print(first_class)
