import grpc

from .protos import common, screencap


class Screencap:
    stub: screencap.ScreencapStub

    def __init__(self, ch: grpc.Channel):
        self.stub = screencap.ScreencapStub(ch)

    def Png(self) -> bytes:
        resp: common.DataChunk = self.stub.Png(common.Empty())
        return resp.data
