# coding=utf-8
import toml


class ConfigManager:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = toml.load(f)

    def get_config_item(self, item_name):
        return self.config[item_name]
