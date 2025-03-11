import bpy

from .save_as_template_operator import SaveAsAppTemplateOperator

def register():
    bpy.utils.register_class(SaveAsAppTemplateOperator)

def unregister():
    bpy.utils.unregister_class(SaveAsAppTemplateOperator)