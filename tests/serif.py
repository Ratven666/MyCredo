from CONFIG import THEODOLITE_SURVEYOR_NETWORK
from base.Point import Point
from base.Project import Project
from measurements.composite_measurments.TotalStationDirections import TotalStationDirection3D

p0 = Point(point_name="p0", x=0, y=0, z=0, is_base_point=True)
p1 = Point(point_name="p1", x=1000, y=0, z=0, is_base_point=True)
p2 = Point(point_name="p2", x=1000, y=1000, z=0, is_base_point=True)
p3 = Point(point_name="p3", x=0, y=1000, z=0, is_base_point=True)

p4 = Point(point_name="p4", x=5500, y=500, z=0, is_base_point=False)

pr = Project(project_name="serif")

pr.add_measurement(TotalStationDirection3D(start_point=p4, end_point=p0, mse_class=THEODOLITE_SURVEYOR_NETWORK))
pr.add_measurement(TotalStationDirection3D(start_point=p4, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK))
pr.add_measurement(TotalStationDirection3D(start_point=p4, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))
pr.add_measurement(TotalStationDirection3D(start_point=p4, end_point=p3, mse_class=THEODOLITE_SURVEYOR_NETWORK))


# pr.add_measurement(HorizontalDistance(start_point=p4, end_point=p0, mse_class=THEODOLITE_SURVEYOR_NETWORK))
# pr.add_measurement(HorizontalDistance(start_point=p4, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK))
# pr.add_measurement(HorizontalDistance(start_point=p4, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))
# pr.add_measurement(HorizontalDistance(start_point=p4, end_point=p3, mse_class=THEODOLITE_SURVEYOR_NETWORK))
#
# pr.add_measurement(Direction(start_point=p4, end_point=p0, mse_class=THEODOLITE_SURVEYOR_NETWORK))
# pr.add_measurement(Direction(start_point=p4, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK))
# pr.add_measurement(Direction(start_point=p4, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))
# pr.add_measurement(Direction(start_point=p4, end_point=p3, mse_class=THEODOLITE_SURVEYOR_NETWORK))

# pr.plot()

print(pr.mse_df)

"""
[0.02508192 0.21546805]
p4_x    0.025082
p4_y    0.215468
Name: mse, dtype: float64
"""