import logging

class BpyService:

    logger = logging.getLogger(__name__)

    @classmethod
    def setup(cls):
        import bpy
        cls.bpy = bpy

    @classmethod
    def save_as(cls, filepath):
        cls.logger.info(f"Save file '{filepath}'")
        cls.bpy.ops.wm.save_as_mainfile(filepath=filepath, copy=True)
