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
from messhes.utils import color_helpers


def materials_exists():
    """Returns True if blendfile has at least one material."""
    return bool(bpy.data.materials)


def is_viewport_colored():
    """Returns True if Blender's materials viewport color is not the default
    color.
    """
    if not materials_exists():
        return False
    
    for material in bpy.data.materials:
        color = tuple(material.diffuse_color)
        if color_helpers.is_default_color(color):
            return False
    
    return True
