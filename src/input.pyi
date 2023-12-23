from enum import Enum

import grpc

class Keycodes:
    """
    input.Keyevent 使用的 keycode
    """

    HOME = "KEYCODE_HOME"
    MENU = "KEYCODE_MENU"
    BACK = "KEYCODE_BACK"
    WAKEUP = "KEYCODE_WAKEUP"
    POWER = "KEYCODE_POWER"
    VOLUME_MUTE = "KEYCODE_VOLUME_MUTE"
    VOLUME_UP = "KEYCODE_VOLUME_UP"
    VOLUME_DOWN = "KEYCODE_VOLUME_DOWN"

class Input:
    def __init__(self, ch: grpc.Channel): ...
    def Text(self, text: str): ...
    def Keyevent(self, longpress: bool, *keycode: str): ...
    def Tap(self, point: tuple[int, int]): ...
    def Swipe(
        self, start: tuple[int, int], end: tuple[int, int], duration: int = 200
    ): ...
    def Draganddrop(
        self, start: tuple[int, int], end: tuple[int, int], duration: int = 200
    ): ...
    def Motionevent(self, event: str, point: tuple[int, int]): ...
