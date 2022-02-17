from typing import Sequence, Type
from mesh_plotter.animator_core import AnimatorBase
from mesh_plotter.meshes import MeshBase

class Animator3D(AnimatorBase):
    def __init__(self, xlim=(-1.,1.), ylim=(-1.,1.), zlim=(0.,1.)):
        super(Animator3D, self).__init__()
        self.ax = self.fig.add_subplot(projection="3d")
        self.xlim = xlim
        self.ylim = ylim
        self.zlim = zlim

    def _animate_impl(self, t: float, meshes: Sequence[Type[MeshBase]]):
        self.ax.cla()
        for mesh in meshes:
            for line in mesh.lines:
                self.ax.plot(line.getXArray(), line.getYArray(), line.getZArray(),
                             color=line.color, linestyle=line.spec)
        self.ax.set_xlim(self.xlim)
        self.ax.set_ylim(self.ylim)
        self.ax.set_zlim(self.zlim)
        self.ax.set_box_aspect((self.xlim[1]-self.xlim[0], self.ylim[1]-self.ylim[0], self.zlim[1]-self.zlim[0]))
        self.ax.set_title("Time: {:.2f} s".format(t))
