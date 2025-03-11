import logging
import os

logger = logging.getLogger(__name__)


def ensure_path_exists(path):
    if not os.path.exists(path):
        logger.warning(f"Create missing folder path : {path}")
        os.makedirs(path)