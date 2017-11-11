# coding=utf-8
from unittest import TestCase
from wakame.config_manager import ConfigManager


class TestConfigManager(TestCase):
    def test_get_config_item(self):
        cm = ConfigManager('../setup.toml')
        self.assertEqual('.', cm.get_config_item('work_dir'))
        self.assertEqual('.', cm.get_config_item('deploy_dir'))
        self.assertEqual('templates', cm.get_config_item('template_path'))
        self.assertEqual('static/img', cm.get_config_item('image_path'))
