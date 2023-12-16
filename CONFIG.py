from accuracy_classes.AccuracyClass import AccuracyClass

MU_0 = 30

REFERENCE_SURVEYOR_NETWORK = AccuracyClass(angle_mse=20,
                                           azimuth_mse=30,
                                           distance_mse=0.03)

THEODOLITE_SURVEYOR_NETWORK = AccuracyClass(angle_mse=40,
                                            azimuth_mse=30,
                                            distance_mse=0.05)
