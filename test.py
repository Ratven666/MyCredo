from CONFIG import THEODOLITE_SURVEYOR_NETWORK
from base.Point import Point
from measurements.directions.Direction import Direction
from measurements.distances.HorizontalDistance import HorizontalDistance
from measurements.composite_measurments.TotalStationDirections import TotalStationDirection3D, TotalStationDirection2D

p0 = Point(point_name="p0", x=0, y=0, z=0, is_base_point=False)
p1 = Point(point_name="p1", x=50, y=50, z=50, is_base_point=False)

tsd1 = TotalStationDirection3D(start_point=p0, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK)
tsd2 = TotalStationDirection2D(start_point=p0, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK)
dist1 = HorizontalDistance(start_point=p0, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK)
dir1 = Direction(start_point=p0, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK)
print(tsd1)
print(tsd1.p)
print(tsd1.get_p_df().info())
print(tsd1.get_p_df())

print()
print(tsd2)
print(tsd2.p)
print(tsd2.get_p_df().info())
print(tsd2.get_p_df())

# print()
#
# print(dist1)
# print(dist1.p)
# print(dist1.get_p_df())
#
# print()
# print(dir1)
# print(dir1.p)
# print(dir1.get_p_df())