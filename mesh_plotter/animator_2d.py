from typing import Sequence, Type
from mesh_plotter.animator_core import AnimatorBase
from mesh_plotter.meshes import MeshBase

class Animator2D(AnimatorBase):
    def __init__(self, xlim=(-1.,1.), ylim=(-1.,1.)):
        super(Animator2D, self).__init__()
        self.ax = self.fig.add_subplot()
        self.xlim = xlim
        self.ylim = ylim
    
    def _animate_impl(self, t: float, meshes: Sequence[Type[MeshBase]]):
        self.ax.cla()
        for mesh in meshes:
            for line in mesh.lines:
                self.ax.plot(line.getXArray(), line.getYArray(),
                             color=line.color, linestyle=line.spec)
        self.ax.set_xlim(self.xlim)
        self.ax.set_ylim(self.ylim)
        self.ax.set_title("Time: {:.2f} s".format(t))
