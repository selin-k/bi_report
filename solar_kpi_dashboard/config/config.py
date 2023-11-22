# filename: solar_kpi_dashboard/config/config.py
import yaml
import os

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            # Determine the absolute path to the config.yaml file
            base_dir = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(base_dir, 'config.yaml')
            with open(config_path, 'r') as f:
                cls._instance.config = yaml.safe_load(f)
        return cls._instance

    @property
    def settings(self):
        return self._instance.config

# Example usage:
# config = Config().settings
# project_name = config['ProjectName']