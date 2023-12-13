from Calculator import Calculator
from Point import Point
from Project import Project
from Station import Station
from measurements.Azimuth import Azimuth
from measurements.Direction import Direction
from measurements.Distance import Distance

p0 = Point(point_name="p0", x=0, y=0, z=0, is_base_point=True)
p1 = Point(point_name="p1", x=0, y=50, z=0, is_base_point=False)
p2 = Point(point_name="p2", x=50, y=100, z=0, is_base_point=False)
p3 = Point(point_name="p3", x=50, y=150, z=0, is_base_point=False)
p4 = Point(point_name="p4", x=100, y=150, z=10, is_base_point=False)
p5 = Point(point_name="p5", x=150, y=200, z=0, is_base_point=False)

project= Project("Hod")

st1 = Station(station_point=p1)
st2 = Station(station_point=p2)
st3 = Station(station_point=p3)
st4 = Station(station_point=p4)

p1_dir0 = Direction(start_point=p1, end_point=p0)
p1_dir2 = Direction(start_point=p1, end_point=p2)

st1.add_measurement(Distance(start_point=p1, end_point=p0))
st1.add_measurement(Distance(start_point=p1, end_point=p2))
st1.add_measurement(Azimuth(start_point=p1, end_point=p0))

st1.add_measurement(p1_dir0)
st1.add_measurement(p1_dir2)

p2_dir1 = Direction(start_point=p2, end_point=p1)
p2_dir3 = Direction(start_point=p2, end_point=p3)

# st2.add_measurement(Distance(start_point=p2, end_point=p1))
st2.add_measurement(Distance(start_point=p2, end_point=p3))

st2.add_measurement(p2_dir1)
st2.add_measurement(p2_dir3)

p3_dir2 = Direction(start_point=p3, end_point=p2)
p3_dir4 = Direction(start_point=p3, end_point=p4)

# st3.add_measurement(Distance(start_point=p3, end_point=p2))
st3.add_measurement(Distance(start_point=p3, end_point=p4))

st3.add_measurement(p3_dir2)
# st3.add_measurement(p3_dir4)

p4_dir3 = Direction(start_point=p4, end_point=p3)
p4_dir5 = Direction(start_point=p4, end_point=p5)

# st4.add_measurement(Distance(start_point=p4, end_point=p3))
# st4.add_measurement(Distance(start_point=p4, end_point=p5))

# st4.add_measurement(p4_dir3)
# st4.add_measurement(p4_dir5)


project.add_station(st1)
project.add_station(st2)
project.add_station(st3)
project.add_station(st4)

# project.plot(scale=10)

project.calculate()





# import pandas as pd
#
# df = pd.DataFrame(columns=["p1_x, p2_x, p3_x"])
# df2 = pd.DataFrame([{"p1_x": 1, "p2_x": 0, "p3_x": 5, "p4_x": 6}], index=["q1"])
# df3 = pd.DataFrame([{"p1_x": 2, "p2_x": 7, "p3_x": 4, "p6_y": 6}], index=["q2"])
#
# d = {"p1_x": 2, "p2_x": 7, "p3_x": 4}
# df = pd.concat([df2, df3]).fillna(0)
# print(df)
