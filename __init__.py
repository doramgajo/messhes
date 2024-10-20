# -*- coding: utf-8 -*-

"""
------------------------------------------------------------
> MESSHES

- AUTHOR:       Doramas García Jorge
- EMAIL:        doramgajo@gmail.com
- GITHUB:       https://github.com/doramgajo
- REPOSITORY:   https://github.com/doramgajo/messhes
- LINKEDIN:     https://www.linkedin.com/in/doramgajo
------------------------------------------------------------
"""

# Blender modules
import bpy

# Messhes modules
from messhes.user_interface import panels
from messhes.user_interface import surface_panels
from messhes.operators import surface_operators


bl_info = {
    "name": "Messhes",
    "author": "Doramas García Jorge",
    "version": (0, 0, 1),
    "blender": (4, 1, 1),
    "description": "Messhes is a Blender addon with multiple functionalities.",
    "location": "View3D > Sidebar > Messhes Tab",
    "warning": "This is an experimental under-development addon.",
    "category": "3D View"
}

classes = [
    # Panels
    panels.MESSHES_PT_main_panel,
    surface_panels.MESSHES_PT_surface_tools,

    # Operators
    surface_operators.MESSHES_OT_toggle_viewport_colors
]


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
