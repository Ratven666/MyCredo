from CONFIG import THEODOLITE_SURVEYOR_NETWORK
from base.Point import Point
from base.Project import Project
from measurements.MeasuredPoint import MeasuredPoint
from measurements.composite_measurments.TotalStationDirections import TotalStationDirection3D, TotalStationDirection2D

p0 = Point(point_name="p0", x=0, y=0, z=0, is_base_point=False)
p1 = Point(point_name="p1", x=1, y=50, z=0, is_base_point=False)
p2 = Point(point_name="p2", x=100, y=150, z=0, is_base_point=False)

pr = Project(project_name="polar")

pr.add_measurement(MeasuredPoint(measured_point=p0, m_x=0.05, m_y=0.05, m_z=0.05))
pr.add_measurement(MeasuredPoint(measured_point=p1, m_x=0.01, m_y=0.05, m_z=0.05))

pr.add_measurement(TotalStationDirection3D(start_point=p1, end_point=p0, mse_class=THEODOLITE_SURVEYOR_NETWORK))
pr.add_measurement(TotalStationDirection3D(start_point=p1, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))

# pr.add_measurement(MeasuredPoint(measured_point=p0, m_x=0.05, m_y=0.05, m_z=0.05))
# pr.add_measurement(MeasuredPoint(measured_point=p1, m_x=0.05, m_y=0.05, m_z=0.05))

# pr.add_measurement(TotalStationDirection3D(start_point=p0, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))
# pr.add_measurement(TotalStationDirection3D(start_point=p0, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK))

# pr.add_measurement(Direction(start_point=p0, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))
# pr.add_measurement(Direction(start_point=p0, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK))

# pr.plot()
pr.calculate()
print(pr.mse_df)
# print(pr.k_df.to_numpy())
# print(pr._calculator.a_df)

"""
M       0.057028
a       0.050000
b       0.027425
m_x     0.040325
m_y     0.040325
m_z     0.019393
theta  56.641608
"""