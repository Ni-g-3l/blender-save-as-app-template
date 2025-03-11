import logging

from .blender import (
    operator, menu
)

bpy_modules = (
    operator, menu
)

from .blender.bpy_service import BpyService
from .core.app_template_creator import AppTemplateCreator

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

def register():
    BpyService.setup()
    AppTemplateCreator.dcc_service = BpyService

    for mod in bpy_modules:
        mod.register()

def unregister():
    for mod in bpy_modules:
        mod.unregister()

