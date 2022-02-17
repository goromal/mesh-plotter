from typing import Type
from mesh_plotter.animator_core import AnimatorBase

class Animator2D(AnimatorBase):
    def __init__(self):
        raise NotImplementedError # Requires SO2, SE2 implementations in geometry
