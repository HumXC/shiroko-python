from .protos import common, window


class Window:
    stub: window.WindowStub

    def __init__(self, ch):
        self.stub = window.WindowStub(ch)

    def GetSize(self):
        resp: window.Size = self.stub.GetSize(common.Empty())
        return resp.width, resp.height

    def SetSize(self, width, height):
        _ = self.stub.SetSize(window.Size(width=width, height=height))

    def GetDensity(self):
        resp: window.Density = self.stub.GetDensity(common.Empty())
        return resp.density

    def SetDensity(self, density):
        _ = self.stub.SetDensity(window.Density(density=density))

    def ResetSize(self):
        _ = self.stub.ResetSize(common.Empty())

    def ResetDensity(self):
        _ = self.stub.ResetDensity(common.Empty())

    def SetRotation(self, lock, rotation):
        _ = self.stub.SetRotation(window.Rotation(lock=lock, rotation=rotation))
