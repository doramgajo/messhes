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


class MESSHES_PT_main_panel(Panel):
    bl_idname = "MESSHES_PT_main_panel"
    bl_category = "Messhes"
    bl_label = "Messhes tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"

    def draw(self, context):
        pass
