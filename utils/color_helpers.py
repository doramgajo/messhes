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


def get_colors():
    """Returns a tuple of predefined colors."""
    return (
        (0.0, 0.0, 0.0, 1.0),  # Black
        (1.0, 0.0, 0.0, 1.0),  # Red
        (0.0, 1.0, 0.0, 1.0),  # Green
        (0.0, 0.0, 1.0, 1.0),  # Blue
        (1.0, 1.0, 0.0, 1.0),  # Yellow
        (1.0, 0.0, 1.0, 1.0),  # Magenta
        (0.0, 1.0, 1.0, 1.0),  # Cyan
        (1.0, 0.5, 0.0, 1.0),  # Orange
        (1.0, 1.0, 1.0, 1.0)   # White
    )


def get_default_color():
    """Returns Blender's default materials viewport color."""
    return 0.8, 0.8, 0.8, 1.0


def is_default_color(color):
    """Returns True if received color is Blender's default materials 
    viewport color.
    """
    color = tuple(round(value, 2) for value in color)
    return color == get_default_color()
