import logging
import os
import shutil
import zipfile

from ..utils import ensure_path_exists

class AppTemplateItems:

    STARTUP = "startup.blend"
    INIT = "__init__.py"
    SPLASH = "splash.png"

    ALL = (STARTUP, INIT, SPLASH)

    BUILD = "dist"


class AppTemplateCreator:

    dcc_service = None

    logger = logging.getLogger(__name__)

    @classmethod
    def save(cls, app_template_name, app_template_root,
             splash_screen_path=None
        ):
        app_template_folder = cls._create_app_template_folder(
            app_template_name, app_template_root
        )

        cls._create_app_template_blends(app_template_folder)
        cls._create_init_file_if_not_exists(app_template_folder)

        if splash_screen_path:
            cls._copy_splash_screen_file(splash_screen_path, app_template_folder)

        return cls._build_app_template(app_template_name, app_template_folder)

    @classmethod
    def _create_app_template_folder(cls, app_template_name, app_template_root):
        app_template_folder = os.path.join(
            app_template_root, app_template_name
        )
        cls.logger.info(
            f"Create missing app template folder path : {app_template_folder}"
        )
        ensure_path_exists(app_template_folder)
        return app_template_folder

    @classmethod
    def _create_app_template_blends(cls, app_template_folder):
        app_template_blend = os.path.join(
            app_template_folder, AppTemplateItems.STARTUP
        )

        cls.logger.info(f"Create app template file : {AppTemplateItems.STARTUP}")

        cls.dcc_service.save_as(app_template_blend)

    @classmethod
    def _create_init_file_if_not_exists(cls, app_template_folder):
        app_template_init = os.path.join(
            app_template_folder, AppTemplateItems.INIT
        )

        if os.path.exists(app_template_init):
            return

        init_resource_file = os.path.join(os.path.dirname(__file__), "..", "resources", "__init__.py")
        shutil.copyfile(init_resource_file, app_template_init)
        cls.logger.info(f"Create app template file : {AppTemplateItems.INIT}")
    
    @classmethod
    def _copy_splash_screen_file(cls, splash_screen_path, app_template_folder):
        app_template_splash = os.path.join(
            app_template_folder, AppTemplateItems.SPLASH
        )

        cls.logger.info(f"Create app template splash : {AppTemplateItems.SPLASH}")
        shutil.copyfile(splash_screen_path, app_template_splash)

    @classmethod
    def _build_app_template(cls, app_template_name, app_template_folder):
        app_template_build_folder = os.path.join(
            app_template_folder, AppTemplateItems.BUILD
        )
        ensure_path_exists(app_template_build_folder)

        app_template_build_file = os.path.join(
            app_template_folder, AppTemplateItems.BUILD,
            app_template_name + ".zip"
        )

        # create the zip file first parameter path/name, second mode
        with zipfile.ZipFile(app_template_build_file, mode="w") as app_template:
            for filename in AppTemplateItems.ALL:
                src_path = os.path.join(app_template_folder, filename)
                dst_path = os.path.join(app_template_name, filename)
                if os.path.exists(src_path):
                    app_template.write(src_path, dst_path)

        return app_template_build_file
