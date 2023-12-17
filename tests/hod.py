from CONFIG import THEODOLITE_SURVEYOR_NETWORK
from base.Point import Point
from base.Project import Project
from base.Station import Station
from measurements.directions.Azimuth import Azimuth
from measurements.directions.Direction import Direction
from measurements.distances.HorizontalDistance import HorizontalDistance

p0 = Point(point_name="p0", x=0, y=0, z=0, is_base_point=True)
p1 = Point(point_name="p1", x=0, y=50, z=0, is_base_point=False)
p2 = Point(point_name="p2", x=50, y=100, z=0, is_base_point=False)
p3 = Point(point_name="p3", x=50, y=150, z=0, is_base_point=False)
p4 = Point(point_name="p4", x=100, y=150, z=0, is_base_point=False)
p5 = Point(point_name="p5", x=150, y=200, z=0, is_base_point=False)

project= Project("Hod")

st1 = Station(station_point=p1)
st2 = Station(station_point=p2)
st3 = Station(station_point=p3)
st4 = Station(station_point=p4)

p1_dir0 = Direction(start_point=p1, end_point=p0, mse_class=THEODOLITE_SURVEYOR_NETWORK)
p1_dir2 = Direction(start_point=p1, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK)

st1.add_measurement(HorizontalDistance(start_point=p1, end_point=p0, mse_class=THEODOLITE_SURVEYOR_NETWORK))
st1.add_measurement(HorizontalDistance(start_point=p1, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))
st1.add_measurement(Azimuth(start_point=p1, end_point=p0, mse_class=THEODOLITE_SURVEYOR_NETWORK))

st1.add_measurement(p1_dir0)
st1.add_measurement(p1_dir2)

p2_dir1 = Direction(start_point=p2, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK)
p2_dir3 = Direction(start_point=p2, end_point=p3, mse_class=THEODOLITE_SURVEYOR_NETWORK)

# st2.add_measurement(HorizontalDistance(start_point=p2, end_point=p1, mse_class=THEODOLITE_SURVEYOR_NETWORK))
st2.add_measurement(HorizontalDistance(start_point=p2, end_point=p3, mse_class=THEODOLITE_SURVEYOR_NETWORK))

st2.add_measurement(p2_dir1)
st2.add_measurement(p2_dir3)

p3_dir2 = Direction(start_point=p3, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK)
p3_dir4 = Direction(start_point=p3, end_point=p4, mse_class=THEODOLITE_SURVEYOR_NETWORK)

# st3.add_measurement(HorizontalDistance(start_point=p3, end_point=p2, mse_class=THEODOLITE_SURVEYOR_NETWORK))
st3.add_measurement(HorizontalDistance(start_point=p3, end_point=p4, mse_class=THEODOLITE_SURVEYOR_NETWORK))

st3.add_measurement(p3_dir2)
st3.add_measurement(p3_dir4)

p4_dir3 = Direction(start_point=p4, end_point=p3, mse_class=THEODOLITE_SURVEYOR_NETWORK)
p4_dir5 = Direction(start_point=p4, end_point=p5, mse_class=THEODOLITE_SURVEYOR_NETWORK)

# st4.add_measurement(HorizontalDistance(start_point=p4, end_point=p3, mse_class=THEODOLITE_SURVEYOR_NETWORK))
st4.add_measurement(HorizontalDistance(start_point=p4, end_point=p5, mse_class=THEODOLITE_SURVEYOR_NETWORK))

st4.add_measurement(p4_dir3)
st4.add_measurement(p4_dir5)


project.add_station(st1)
project.add_station(st2)
project.add_station(st3)
project.add_station(st4)

# project.plot(scale=10)

project.calculate()

"""
/Users/mikhail_vystrchil/Documents/MY_PROGRAMMS/MyCredo/venv/bin/python /Users/mikhail_vystrchil/Documents/MY_PROGRAMMS/MyCredo/hod2.py 
[0.00498869 0.05       0.02594979 0.05611154 0.02639878 0.06632122
 0.04412364 0.06649819 0.05695529 0.07562419]
 
 [0.0072722  0.05       0.03050503 0.05720055 0.03963649 0.06724509
 0.05311357 0.07176799 0.07335817 0.08827955]"""





# import pandas as pd
#
# df = pd.DataFrame(columns=["p1_x, p2_x, p3_x"])
# df2 = pd.DataFrame([{"p1_x": 1, "p2_x": 0, "p3_x": 5, "p4_x": 6}], index=["q1"])
# df3 = pd.DataFrame([{"p1_x": 2, "p2_x": 7, "p3_x": 4, "p6_y": 6}], index=["q2"])
#
# d = {"p1_x": 2, "p2_x": 7, "p3_x": 4}
# df = pd.concat([df2, df3]).fillna(0)
# print(df)
