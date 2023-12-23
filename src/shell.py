import io

import grpc

from .protos import common, shell


class Shell:
    stub: shell.ShellStub

    def __init__(self, ch):
        self.stub = shell.ShellStub(ch)

    def Run(self, command, timeout=0):
        """执行命令。

        Args:
            command (str): 需要执行的命令。
            timeout (int): 超时时间，超时之后将强制返回。

        Returns:
            bytes: 返回的数据
        """
        resp: common.DataChunk = self.stub.Run(
            shell.RunRequest(cmd=command, timeout_ms=timeout)
        )
        return resp.data

    def Push(self, file: io.BufferedReader, filname: str):
        """向设备发送一个文件。

        Args:
            file (io.BytesIO): 需要发送的文件。
            filname (str): 文件储存在设备上的文件名。
        """
        push: grpc.StreamUnaryMultiCallable = self.stub.Push
        while True:
            chunk: bytes = file.read(1024 * 1024)
            if not chunk:
                break
            print("push", len(chunk))
            push.future(shell.PushRequest(data=chunk, filename=filname))

    def Pull(self, filename: str):
        """从设备上获取文件，返回迭代器。

        Args:
            filename (str): 文件名。

        Yields:
            bytes: 文件数据
        """
        pull: grpc.UnaryStreamMultiCallable = self.stub.Pull
        for resp in pull(shell.PullRequest(filename=filename)):
            yield resp.data

    def Install(self, apkpath: str):
        """在设备上安装 apk。

        Args:
            apkpath (str): apk 文件在设备上的位置。
        """
        _ = self.stub.Install(shell.InstallRequest(apkpath=apkpath))

    def Uninstall(self, pkgname):
        """卸载一个程序。

        Args:
            pkgname (str): 需要卸载的程序包名。
        """
        _ = self.stub.Uninstall(shell.UninstallRequest(pkgname=pkgname))

    def ListApps(self):
        """获取在设备上的所有包名。

        Returns:
            list[str]: 包名列表。
        """
        resp: shell.ListAppsResponse = self.stub.ListApps(common.Empty())
        return resp.apps

    def StartApp(self, active):
        """启动一个应用，参考安卓命令: "am start"。

        Args:
            active (str): 启动的参数，<包名/Active路径>
        """
        _ = self.stub.StartApp(shell.StartAppRequest(active=active))

    def StopApp(self, pkgname):
        """终止一个应用。

        Args:
            pkgname (str): 应用包名。
        """
        _ = self.stub.StopApp(shell.StopAppRequest(pkgname=pkgname))

    def Getprop(self, key: str):
        """安卓命令 "getprop".

        Args:
            key (str): 键名。

        Returns:
            str: 值。
        """
        resp: shell.GetpropResponse = self.stub.Getprop(shell.GetpropRequest(key=key))
        return resp.value
