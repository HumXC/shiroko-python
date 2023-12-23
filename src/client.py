import grpc

from .manager import Manager
from .shell import Shell


class Client:
    manager: Manager
    shell: Shell

    def __init__(self, addr: str):
        ch = grpc.insecure_channel(addr)
        self.manager = Manager(ch)
        self.shell = Shell(ch)
