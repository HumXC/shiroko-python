import socket
import time
from dataclasses import dataclass

from zeroconf import ServiceBrowser, ServiceListener, Zeroconf


@dataclass
class ServiceInfo:
    """Shiroko 服务端的信息"""

    addr: str
    name: str
    model: str


class __listener(ServiceListener):
    results: list[ServiceInfo]

    def __init__(self, results: list[ServiceInfo]) -> None:
        super().__init__()
        self.results = results

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        if info is None:
            return
        ip = socket.inet_ntoa(info.addresses[0])
        port = ""
        model = ""
        name = info.name.replace("." + info.type, "")
        # 为什么 info.text 以 \x0c 开头。。
        for t in info.text.decode("utf-8").replace("\x0c", "").split("\n"):
            kv = t.split("=")
            if kv[0] == "model":
                model = kv[1]
            if kv[0] == "port":
                port = kv[1]
        self.results.append(ServiceInfo(ip + ":" + port, name, model))


def FindServer(timeout: int) -> list[ServiceInfo]:
    """在局域网里搜索运行了 shiroko 的设备。
       由于安卓的电源策略，设备在锁屏时可能无法被搜索到。

    Args:
        timeout (int): 搜索的时间，超时后返回结果。

    Returns:
        ServiceInfo: shiroko 服务的信息
    """
    results: list[ServiceInfo] = []
    zeroconf = Zeroconf()
    listener = __listener(results)
    _ = ServiceBrowser(zeroconf, "_shiroko._tcp.local.", listener)
    time.sleep(timeout)
    zeroconf.close()
    return results
