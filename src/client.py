import grpc

from .manager import Manager


class Client:
    manager: Manager

    def __init__(self, addr: str):
        ch = grpc.insecure_channel(addr)
        self.manager = Manager(ch)
