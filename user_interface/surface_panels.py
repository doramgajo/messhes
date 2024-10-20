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

# Blender classes
from bpy.types import Panel

# Messhes modules
from messhes.operators.operator_helpers import surface_helpers
from messhes.utils.blender_functions import blender_materials


class MESSHES_PT_surface_tools(Panel):
    bl_idname = "MESSHES_PT_surface_tools"
    bl_parent_id = "MESSHES_PT_main_panel"
    bl_category = "Messhes"
    bl_label = "Surface tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_label = "Surface tools"
    bl_order = 0


    def draw(self, context):
        layout = self.layout
        layout.operator("messhes.toggle_viewport_colors",
                        text=surface_helpers.get_toggle_viewport_button_text(),
                        icon=surface_helpers.get_toggle_viewport_button_icon(),
                        depress=blender_materials.is_viewport_colored()
                        )
