from CONFIG import THEODOLITE_SURVEYOR_NETWORK
from base.Point import Point
from base.Project import Project
from measurements.composite_measurments.TotalStationDirections import TotalStationDirection3D

p0 = Point(point_name="p0", x=0, y=0, z=0, is_base_point=True)
p1 = Point(point_name="p1", x=0, y=50, z=0, is_base_point=True)
p2 = Point(point_name="p2", x=100, y=200, z=50, is_base_point=False)

pr = Project(project_name="polar")

pr.add_measurement(TotalStationDirection3D(start_point=p1, end_point=p0, mse_class=THEODOLITE_SURVEYOR_NETWORK))
pr.add_measurement(TotalStationDirection3D(start_point=p1, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))
# pr.add_measurement(TotalStationDirection3D(start_point=p0, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))
# pr.add_measurement(TotalStationDirection3D(start_point=p0, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK))

# pr.add_measurement(Direction(start_point=p0, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))
# pr.add_measurement(Direction(start_point=p0, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK))

# pr.plot()
print(pr.mse_df)