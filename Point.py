

class Point:

    __points_name = set()

    def __init__(self, point_name: str,
                 x: float, y: float, z: float, is_base_point: bool):
        self.point_name = self.__check_point_name(point_name=point_name)
        self.x = x
        self.y = y
        self.z = z
        self.is_base_point = is_base_point

    def __repr__(self):
        return (f"{self.__class__.__name__}(point_name={self.point_name}, "
                f"x={self.x}, y={self.y}, z={self.z}, is_base_point={self.is_base_point})")

    def __str__(self):
        return f"{self.__class__.__name__}(point_name={self.point_name})"

    def __eq__(self, other):
        return self.point_name == other.point_name

    def __check_point_name(self, point_name):
        if point_name in self.__points_name:
            raise ValueError(f"Точка с именем \"{point_name}\" уже существует!")
        else:
            self.__points_name.add(point_name)
            return point_name


if __name__ == "__main__":
    p1 = Point(point_name="p1", x=10, y=10, z=0, is_base_point=True)
    p2 = Point(point_name="p2", x=20, y=20, z=0, is_base_point=False)
    p_lst = [p1, p2]
    print(p1)
    print(p_lst)
    p2.point_name = "p1"
    print(p1 == p2)
    print(p1 == p1)
    p3 = p2.__class__(point_name="p3", x=1, y=2, z=3, is_base_point=True)
    print(p3)
