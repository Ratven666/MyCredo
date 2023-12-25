from CONFIG import THEODOLITE_SURVEYOR_NETWORK
from base.Point import Point
from base.Project import Project
from measurements.MeasuredPoint import MeasuredPoint
from measurements.composite_measurments.TotalStationDirections import TotalStationDirection3D
from measurements.directions.Direction import Direction
from measurements.distances.HorizontalDistance import HorizontalDistance

p0 = Point(point_name="p0", x=0, y=0, z=0, is_base_point=True)
p1 = Point(point_name="p1", x=1000, y=0, z=0, is_base_point=True)
p2 = Point(point_name="p2", x=1000, y=1000, z=0, is_base_point=True)
p3 = Point(point_name="p3", x=0, y=1000, z=0, is_base_point=True)

p4 = Point(point_name="p4", x=1500, y=500, z=0, is_base_point=False)

pr = Project(project_name="serif")

pr.add_measurement(TotalStationDirection3D(start_point=p4, end_point=p0, mse_class=THEODOLITE_SURVEYOR_NETWORK))
pr.add_measurement(TotalStationDirection3D(start_point=p4, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK))
pr.add_measurement(TotalStationDirection3D(start_point=p4, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))
pr.add_measurement(TotalStationDirection3D(start_point=p4, end_point=p3, mse_class=THEODOLITE_SURVEYOR_NETWORK))

pr.add_measurement(MeasuredPoint(measured_point=p4, m_x=0.05, m_y=0.05, m_z=0.05))

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
M       0.053476
a       0.045244
b       0.028506
m_x     0.028506
m_y     0.045244
m_z          NaN
theta  90.000000
"""