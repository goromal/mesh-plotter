from typing import Sequence, Union, Type
import numpy as np
from geometry import SO3, SE3
from pysignals import LinearInterpolator
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mesh_plotter.meshes import MeshBase
from mesh_plotter.transforms import applyTransformToMesh

class MeshSequence(object):
    def __init__(self, mesh : Type[MeshBase], transforms : Sequence[Union[SO3,SE3]], t : Sequence[float]):
        self.mesh = mesh
        self.transforms = transforms
        self.t = t

class AnimatorBase(object):
    def __init__(self):
        self.fig = plt.figure()
        self.mesh_sequences: Sequence[MeshSequence] = []
        self.mesh_interpolators: Sequence[LinearInterpolator] = []

    def addMeshSequence(self, mesh : Type[MeshBase], transforms : Sequence[Union[SO3,SE3]], t : Sequence[float]):
        self.mesh_sequences.append(MeshSequence(mesh, transforms, t))
        self.mesh_interpolators.append(LinearInterpolator(t, transforms))

    def animate(self, dt : float = 0.1):
        t_min = np.inf
        t_max = -np.inf
        for mesh_sequence in self.mesh_sequences:
            mst_min = min(mesh_sequence.t)
            mst_max = max(mesh_sequence.t)
            if mst_min < t_min:
                t_min = mst_min
            if mst_max > t_max:
                t_max = mst_max
        num_frames = int(np.floor((t_max - t_min) / dt))
        t_query = np.linspace(t_min, t_max, num_frames)

        interpolated_mesh_sequences = []
        for mesh_sequence, mesh_interpolator in zip(self.mesh_sequences, self.mesh_interpolators):
            new_transforms = []
            for i in range(num_frames):
                new_transforms.append(mesh_interpolator.at(t_query[i]))
            interpolated_mesh_sequences.append(MeshSequence(
                mesh = mesh_sequence.mesh, 
                transforms = new_transforms, 
                t = t_query
            ))

        anim = animation.FuncAnimation(self.fig, self._animate, frames=num_frames, interval=int(1000.0*dt),
                                       fargs=(t_query, interpolated_mesh_sequences,), blit=False)
        plt.show()

    def _animate(self, i: int, t: Sequence[float], ims: Sequence[MeshSequence]):
        meshes = [applyTransformToMesh(im.transforms[i], im.mesh) for im in ims]
        self._animate_impl(t[i], meshes)

    def _animate_impl(self, t: float, meshes: Sequence[Type[MeshBase]]):
        raise NotImplementedError()
