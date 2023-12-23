from .protos import input


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
    stub: input.InputStub

    def __init__(self, ch):
        self.stub = input.InputStub(ch)

    def Text(self, text: str):
        """向输入框输入文本，仅支持英文。

        Args:
            text (str): 需要输入的文本，仅支持英文。
        """
        self.stub.Text(input.TextRequest(text=text))

    def Keyevent(self, longpress: bool, *keycode: str):
        """发送 keyevent 事件。

        Args:
            longpress (bool): 是否长按.
            keycode (list[str]): 例如[KEYCODE_HOME], 参考: https://developer.android.com/reference/android/view/KeyEvent#constants_1
        """
        self.stub.Keyevent(input.KeyeventRequest(keycode=keycode, longpress=longpress))

    def Tap(self, point: tuple[int, int]):
        """点击屏幕上的坐标。

        Args:
            point (tuple[int, int]): 坐标 (x, y)。
        """
        self.stub.Tap(input.TapRequest(x=point[0], y=point[1]))

    def Swipe(self, start: tuple[int, int], end: tuple[int, int], duration=200):
        """在屏幕上滑动。

        Args:
            start (tuple[int, int]): 开始坐标 (x, y)。
            end (tuple[int, int]): 结束坐标 (x, y)。
            duration (int, optional): 持续时间，单位 ms, 默认值 200.
        """
        self.stub.Swipe(
            input.SwipeRequest(
                x1=start[0], y1=start[1], x2=end[0], y2=end[1], duration=duration
            )
        )

    def Draganddrop(self, start: tuple[int, int], end: tuple[int, int], duration=200):
        """在屏幕模拟拖放动作。

        Args:
            start (tuple[int, int]): 开始坐标 (x, y)。
            end (tuple[int, int]): 结束坐标 (x, y)。
            duration (int, optional): 持续时间，单位 ms, 默认值 200.
        """
        self.stub.Draganddrop(
            input.DraganddropRequest(
                x1=start[0], y1=start[1], x2=end[0], y2=end[1], duration=duration
            )
        )

    def Motionevent(self, event, point):
        """模拟屏幕运动操作。

        Args:
            event (str): 参考: https://developer.android.com/reference/android/view/MotionEvent#constants_1
            point (tuple[int, int]): 事件发生的位置 (x. y).
        """
        self.stub.Motionevent(
            input.MotioneventRequest(event=event, x=point[0], y=point[1])
        )
