"""
Application Logging Configuration
"""

import logging


def setup_logging():
    """
    Configure application logging.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    logger = logging.getLogger("cloud-copilot")

    return logger


logger = setup_logging()