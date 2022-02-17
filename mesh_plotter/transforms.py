from typing import Union
from geometry import SO3, SE3
from mesh_plotter.meshes import Line, MeshBase

def applyTransformToMesh(X : Union[SO3,SE3], mesh : MeshBase) -> MeshBase:
    new_lines = []
    for line in mesh.lines:
        new_points = []
        for point in line.points:
            new_points.append(X * point)
        new_lines.append(Line(points=new_points, color=line.color, spec=line.spec))
    return MeshBase(lines=new_lines)
