import grpc
from SLAM.mhist_api.rpc_pb2_grpc import MhistStub
from SLAM.mhist_api.rpc_pb2 import MeasurementMessage, Measurement, Raw
import numpy as np
import time


channel = grpc.insecure_channel("localhost:6666")
stub = MhistStub(channel)

while True:
    range_data = np.random.normal()
    mu, sigma = 120, 50 # mean and standard deviation
    s = np.random.normal(mu, sigma, 1000)
    s = s[s>0]
    for r in range(360):
        stub.Store(MeasurementMessage(
            name="sensor_data",
            measurement=Measurement(
                raw=Raw(value="{0}-{1}".format(r, s[r]).encode()))))
        time.sleep(0.05)
