from Calculator import Calculator
from Point import Point
from Project import Project
from Station import Station
from measurements.Azimuth import Azimuth
from measurements.Direction import Direction
from measurements.Distance import Distance

p0 = Point(point_name="p0", x=0, y=0, z=0, is_base_point=True)
p1 = Point(point_name="p1", x=500, y=0, z=0, is_base_point=True)
p2 = Point(point_name="p2", x=500, y=500, z=0, is_base_point=True)
p3 = Point(point_name="p3", x=0, y=500, z=0, is_base_point=True)
p4 = Point(point_name="p4", x=250, y=200, z=10, is_base_point=False)
p5 = Point(point_name="p5", x=250, y=300, z=0, is_base_point=False)

p_lst = [p0, p1, p2, p3, p4, p5]

l1 = Distance(p4, p0)
l2 = Distance(p4, p1)
l3 = Distance(p4, p2)

az1 = Azimuth(p4, p0)
az2 = Azimuth(p4, p1)
az3 = Azimuth(p4, p2)

l4 = Distance(p5, p3)
l5 = Distance(p5, p2)
l6 = Distance(p5, p4)

az4 = Azimuth(p5, p3)
az5 = Azimuth(p5, p2)
az6 = Azimuth(p5, p4)

dir1 = Direction(p4, p0)
dir2 = Direction(p4, p1)
dir3 = Direction(p4, p2)
dir4 = Direction(p4, p3)

dir5 = Direction(p5, p4)
dir6 = Direction(p5, p2)
dir7 = Direction(p5, p3)


# dir1 = Direction(p4, p3, mse=0)
#
# az1 = Azimuth(p0, p3, mse=0)
# az2 = Azimuth(p4, p3, mse=0)

station0 = Station(station_point=p4)
# station1 = Station(station_point=p5)

station0.add_measurement(dir1)
station0.add_measurement(dir2)
station0.add_measurement(dir3)
station0.add_measurement(dir4)

# station0.add_measurement(az1)
# station0.add_measurement(az2)
# station0.add_measurement(az3)

# station0.add_measurement(l1)
# station0.add_measurement(l2)
# station0.add_measurement(l3)

# station1.add_measurement(az4)
# station1.add_measurement(az5)
# station1.add_measurement(az6)

# station1.add_measurement(l4)
# station1.add_measurement(l5)
# station1.add_measurement(l6)

# station1.add_measurement(dir5)
# station1.add_measurement(dir6)
# station1.add_measurement(dir7)

# station1.add_measurement(dir1)
# station1.add_measurement(az2)

project = Project(project_name="test")

project.add_points(p_lst)
project.add_station(station0)
# project.add_station(station1)

calculator = Calculator(project)
calculator.calculate()

# print(calculator.a_df)

a = calculator.a_df.to_numpy()

for st in calculator.project.stations.values():
    print(st)
    # print(st.a_df)
# print(a)

print(calculator.a_df)
print(calculator.p_df)

# project.plot(scale=30)
