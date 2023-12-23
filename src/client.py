import grpc

from .input import Input
from .manager import Manager
from .screencap import Screencap
from .shell import Shell
from .window import Window


class Client:
    manager: Manager
    shell: Shell
    input: Input
    screencap: Screencap
    window: Window

    def __init__(self, addr: str):
        ch = grpc.insecure_channel(addr)
        self.manager = Manager(ch)
        self.shell = Shell(ch)
        self.input = Input(ch)
        self.screencap = Screencap(ch)
        self.window = Window(ch)
