from typing import Sequence
import numpy as np

class Line(object):
    def __init__(self, points : Sequence[np.ndarray], color : str = 'black', spec : str = '-'):
        self.points = points
        self.color = color
        self.spec = spec

    def getXArray(self):
        return [point[0] for point in self.points]

    def getYArray(self):
        return [point[1] for point in self.points]

    def getZArray(self):
        return [point[2] for point in self.points]

class MeshBase(object):
    def __init__(self, lines : Sequence[Line] = [], scale : float = None):
        self.lines : Sequence[Line] = lines
        if scale is not None:
            for line in self.lines:
                for point in line.points:
                    point *= scale

class Axes3DMesh(MeshBase):
    def __init__(self, scale : float = 1.0):
        x_axis = Line(
            points = [np.array([0.,0.,0.]), np.array([1.,0.,0.])],
            color = "red",
        )
        y_axis = Line(
            points = [np.array([0.,0.,0.]), np.array([0.,1.,0.])],
            color = "green",
        )
        z_axis = Line(
            points = [np.array([0.,0.,0.]), np.array([0.,0.,1.])],
            color = "blue",
        )
        super(Axes3DMesh, self).__init__(
            lines = [x_axis, y_axis, z_axis],
            scale = scale
        )
