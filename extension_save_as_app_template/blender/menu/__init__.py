import bpy

from .save_as_template_menu import menu_func_import

def register():
    bpy.types.TOPBAR_MT_blender.prepend(menu_func_import)

def unregister():
    bpy.types.TOPBAR_MT_blender.remove(menu_func_import)