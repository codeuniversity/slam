import SLAM.core
import grpc
from multiprocessing import Process
from multiprocessing import Queue
from SLAM.mhist_api.rpc_pb2_grpc import MhistStub
from SLAM.mhist_api.rpc_pb2 import Filter
from SLAM.core import Point

class Receiver(Process):
    def __init__(self,queue: Queue):
        super(Receiver, self).__init__()
        self.queue = queue

    def run(self):
        channel = grpc.insecure_channel('localhost:6666')
        stub = MhistStub(channel)

        old_rotation = 0
        point_batch = []

        for message in stub.Subscribe(Filter(names=['sensor_data'])):
            rotation,distance = message.measurement.raw.value.decode().split('-')
            if rotation < old_rotation:
                self.queue.put(point_batch)
                point_batch = []
            point_batch.append([rotation,distance])
            old_rotation = rotation





