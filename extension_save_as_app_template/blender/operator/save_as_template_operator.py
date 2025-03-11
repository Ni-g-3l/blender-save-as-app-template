import bpy
from bpy_extras.io_utils import ExportHelper
from ...core.app_template_creator import AppTemplateCreator

class SaveAsAppTemplateOperator(bpy.types.Operator):

    bl_idname = "app.save_as_app_template"
    bl_label = "Save as App Template"
    bl_options = {'REGISTER'}

    # Define this to tell 'fileselect_add' that we want a directoy
    directory: bpy.props.StringProperty(
        name="Outdir Path",
        description="Where I will save my stuff"
        # But this will be anyway a directory path.
    )

    # Define this to tell 'fileselect_add' that we want a directoy
    filename: bpy.props.StringProperty(
        name="App Template Name",
        description="Where I will save my stuff"
        # subtype='DIR_PATH' is not needed to specify the selection mode.
        # But this will be anyway a directory path.
    )

    # Filters folders
    filter_folder: bpy.props.BoolProperty(
        default=True,
        options={"HIDDEN"}
    )

    splash_screen_path: bpy.props.StringProperty(
        name='Splash Screen File',
        description='Splash Screen File Path',
    )

    auto_install: bpy.props.BoolProperty(
        name='Install App Template',
        description='Automatically install App Template',
        default=True
    )

    def execute(self, _):
        app_template_file = AppTemplateCreator.save(
            self.filename.strip(), self.directory.strip(),
            self.splash_screen_path
        )

        if self.auto_install:
            bpy.ops.preferences.app_template_install(overwrite=True, filepath=app_template_file)

        return {'FINISHED'}

    def invoke(self, context, event):
        # Open browser, take reference to 'self' read the path to selected
        # file, put path in predetermined self fields.
        # See: https://docs.blender.org/api/current/bpy.types.WindowManager.html#bpy.types.WindowManager.fileselect_add
        context.window_manager.fileselect_add(self)
        # Tells Blender to hang on for the slow user input
        return {'RUNNING_MODAL'}
