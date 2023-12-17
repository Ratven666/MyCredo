from CONFIG import THEODOLITE_SURVEYOR_NETWORK
from base.Point import Point
from base.Project import Project
from measurements.directions.Azimuth import Azimuth
from measurements.composite_measurments.TotalStationDirections import TotalStationDirection2D

p0 = Point(point_name="p0", x=0, y=0, z=0, is_base_point=True)
p1 = Point(point_name="p1", x=0, y=50, z=0, is_base_point=False)
p2 = Point(point_name="p2", x=50, y=100, z=0, is_base_point=False)
p3 = Point(point_name="p3", x=50, y=150, z=0, is_base_point=False)
p4 = Point(point_name="p4", x=100, y=150, z=10, is_base_point=False)
p5 = Point(point_name="p5", x=150, y=200, z=0, is_base_point=False)

project = Project(project_name="Hod_2")

project.add_measurement(Azimuth(start_point=p1, end_point=p0, mse_class=THEODOLITE_SURVEYOR_NETWORK))
project.add_measurement(TotalStationDirection2D(start_point=p1, end_point=p0, mse_class=THEODOLITE_SURVEYOR_NETWORK))
project.add_measurement(TotalStationDirection2D(start_point=p1, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))

project.add_measurement(TotalStationDirection2D(start_point=p2, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK))
project.add_measurement(TotalStationDirection2D(start_point=p2, end_point=p3, mse_class=THEODOLITE_SURVEYOR_NETWORK))

project.add_measurement(TotalStationDirection2D(start_point=p3, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))
project.add_measurement(TotalStationDirection2D(start_point=p3, end_point=p4, mse_class=THEODOLITE_SURVEYOR_NETWORK))

project.add_measurement(TotalStationDirection2D(start_point=p4, end_point=p3, mse_class=THEODOLITE_SURVEYOR_NETWORK))
project.add_measurement(TotalStationDirection2D(start_point=p4, end_point=p5, mse_class=THEODOLITE_SURVEYOR_NETWORK))

# project.plot()
# project.calculate()
# print(project.k_df)

print(project.mse_df)