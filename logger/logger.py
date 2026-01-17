import logging
import sys


class Logger:
    _logger = None

    @classmethod
    def _get_logger(cls):
        if cls._logger is None:
            cls._logger = logging.getLogger("selenium_tests")
            cls._logger.setLevel(logging.DEBUG)

            if not cls._logger.handlers:
                handler = logging.StreamHandler(sys.stdout)
                handler.setLevel(logging.DEBUG)
                formatter = logging.Formatter(
                    "%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S"
                )
                handler.setFormatter(formatter)
                cls._logger.addHandler(handler)

        return cls._logger

    @classmethod
    def info(cls, message: str) -> None:
        cls._get_logger().info(message)

    @classmethod
    def debug(cls, message: str) -> None:
        cls._get_logger().debug(message)

    @classmethod
    def warning(cls, message: str) -> None:
        cls._get_logger().warning(message)

    @classmethod
    def error(cls, message: str) -> None:
        cls._get_logger().error(message)
