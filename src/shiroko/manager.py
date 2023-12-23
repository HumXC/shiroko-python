from .protos import common, manager


class Manager:
    stub: manager.ManagerStub

    def __init__(self, ch):
        self.stub = manager.ManagerStub(ch)

    def List(self):
        """列出所有可用的工具的名称。

        Returns:
            list[str]: 所有可用工具的名称。
        """
        resp: manager.ListResponse = self.stub.List(common.Empty())
        return resp.names

    def Health(self, name):
        """检查工具的可用性。

        Args:
            name (str): 需要安装的工具名称。

        Returns:
            str: 关于可用性的描述，如果一切正常，返回 "OK"。
        """
        resp: manager.HealthResponse = self.stub.Health(manager.NameRequest(name=name))
        return resp.status

    def Install(self, name):
        """在设备上部署工具。

        Args:
            name (str): 需要安装的工具名称。
        """
        _ = self.stub.Install(manager.NameRequest(name=name))

    def Uninstall(self, name):
        """卸载工具。

        Args:
            name (str): 需要卸载的工具名称。
        """
        _ = self.stub.Uninstall(manager.NameRequest(name=name))

    def Env(self, name):
        """获取工具使用的环境变量。

        Args:
            name (str): 工具名称。

        Returns:
            list[str]: 环境变量的值
        """
        resp: manager.EnvResponse = self.stub.Env(manager.NameRequest(name=name))
        return resp.envs

    def Exe(self, name):
        """获取工具的执行文件路径或者命令。

        Args:
            name (str): 工具名称。

        Returns:
            str: 工具在设备上的执行文件路径或者命令。
        """
        resp: manager.ExeResponse = self.stub.Exe(manager.NameRequest(name=name))
        return resp.exe

    def Args(self, name):
        """获取工具使用参数列表。

        Args:
            name (str): 工具名称。

        Returns:
            str: 参数列表。
        """
        resp: manager.ArgsResponse = self.stub.Args(manager.NameRequest(name=name))
        return resp.args

    def Files(self, name):
        """获取工具在设备上部署的文件。

        Args:
            name (str): 工具名称。

        Returns:
            str: 文件列表。
        """
        resp: manager.FilesResponse = self.stub.Files(manager.NameRequest(name=name))
        return resp.files
