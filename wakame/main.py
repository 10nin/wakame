# coding=utf-8
import sys
import os
from . import (html_converter, file_manager, config_manager)


class App:
    @staticmethod
    def run(config_path):
        cfg = config_manager.ConfigManager(config_path=config_path)


if __name__ == '__main__':
    # call by command line: %wakame% config_file_path
    App.run(sys.argv[0])
