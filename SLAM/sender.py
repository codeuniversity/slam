import grpc
from SLAM.mhist_api.rpc_pb2_grpc import MhistStub
from SLAM.mhist_api.rpc_pb2 import MeasurementMessage, Measurement, Raw
from SLAM.core import Point
from typing import List

channel = grpc.insecure_channel('localhost:6666')
stub = MhistStub(channel)


def create_raw_measurement(point):
    return Raw(value="{},{}".format(point.x, point.y).encode())


def iter_map_updates(points: List[Point]):
    for p in points:
        yield MeasurementMessage(
            name='map_updates',
            measurement=Measurement(
                raw=create_raw_measurement(p)
            )
        )


def send_points(points):
    stub.StoreStream(iter_map_updates(points))


def send_position(position):
    stub.Store(MeasurementMessage(
        name='position_updates',
        measurement=Measurement(
            raw=create_raw_measurement(position)
        )
    ))
