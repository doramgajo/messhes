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

# Blender classes
from bpy.types import Operator

# Messhes modules
from messhes.utils.blender_functions import blender_materials
from messhes.utils import color_helpers


class MESSHES_OT_toggle_viewport_colors(Operator):
    bl_idname = "messhes.toggle_viewport_colors"
    bl_label = "Toggle viewport colors"

    def execute(self, context):
        if not blender_materials.materials_exists():
            self.report({"INFO"}, "The scene does not have any materials.")
            return {"CANCELLED"}
        
        materials = bpy.data.materials

        return self.discolor(materials) \
            if blender_materials.is_viewport_colored() \
            else self.color(materials)

    def color(self, materials):
        """Color materials viewport color with a list of colors."""
        colors = color_helpers.get_colors()
        number_of_colors = len(colors)
        mod = 0

        for material in materials:
            material.diffuse_color = colors[mod]
            mod = (mod + 1) % number_of_colors
        self.report({"INFO"}, "Viewport colors changed.")
        return {"FINISHED"}


    def discolor(self, materials):
        """Discolor materials viewport color to default color."""
        color = color_helpers.get_default_color()
        for material in materials:
            material.diffuse_color = color
        self.report({"INFO"}, "Viewport colors changed to default.")
        return {"FINISHED"}
