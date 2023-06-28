# Mesh Plotter

![example workflow](https://github.com/goromal/mesh-plotter/actions/workflows/test.yml/badge.svg)

Tools for plotting transforms and line meshes in Python.

## Example

```python
import numpy as np
from geometry import SO3, SE3
from mesh_plotter.meshes import Axes3DMesh
from mesh_plotter.animator_3d import Animator3D

times = [0.0, 5.0, 10.0, 15.0]

se3_1 = SE3.identity()
se3_2 = SE3.fromVecAndQuat(np.array([2.0,0.0,0.0]),
                           SO3.fromEuler(1.5,-2.0,0.2))
se3_3 = SE3.fromVecAndQuat(np.array([-1.5,-1.5,1.5]),
                           SO3.random())

transforms1 = [se3_1]*4
transforms2 = [se3_2]*4
transforms3 = [se3_3]*4
transforms  = [se3_1, se3_2, se3_3, se3_1]

animator = Animator3D(xlim=(-2.5,2.5), ylim=(-2.5,2.5), zlim=(0.,2.))
animator.addMeshSequence(Axes3DMesh(scale=0.4), transforms1, times)
animator.addMeshSequence(Axes3DMesh(scale=0.4), transforms2, times)
animator.addMeshSequence(Axes3DMesh(scale=0.4), transforms3, times)
animator.addMeshSequence(Axes3DMesh(), transforms, times)
animator.animate(dt = 0.1)
```
