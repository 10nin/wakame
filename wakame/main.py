# coding=utf-8
import sys
import os
from . import (html_converter, file_manager, config_manager)


class App:
    def __init__(self):
        self.work_dir = ''
        self.deploy_dir = ''
        self.template_path = ''
        self.image_path = ''

    def run(self,config_path):
        cfg = config_manager.ConfigManager(config_path=config_path)
        self.work_dir = cfg.get_config_item('work_dir')
        self.deploy_dir = cfg.get_config_item('deploy_dir')
        self.template_path = cfg.get_config_item('template_path')
        self.image_path = cfg.get_config_item('image_path')

        hm = html_converter.HtmlConverter()

if __name__ == '__main__':
    # call by command line: %wakame% config_file_path
    app = App()
    app.run(sys.argv[0])
