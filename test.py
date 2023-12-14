from Point import Point
from measurements.Direction import Direction
from measurements.HorizontalDistance import HorizontalDistance
from measurements.TotalStationDirection import TotalStationDirection

p0 = Point(point_name="p0", x=0, y=0, z=0, is_base_point=False)
p1 = Point(point_name="p1", x=50, y=50, z=50, is_base_point=False)

tsd1 = TotalStationDirection(start_point=p0, end_point=p1)
dist1 = HorizontalDistance(start_point=p0, end_point=p1)
dir1 = Direction(start_point=p0, end_point=p1)
print(tsd1)
print(tsd1.p)

print()

print(dist1)
print(dist1.p)
print(dist1.get_p_df())

print()
print(dir1)
print(dir1.p)
print(dir1.get_p_df())