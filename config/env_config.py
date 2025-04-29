import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.yml"

class ENV:
    """动态读取当前环境配置"""
    with open(CONFIG_PATH) as f:
        _config = yaml.safe_load(f.read())

    CURRENT_ENV = _config["env"]
    BASE_URL = _config[CURRENT_ENV]["base_url"]
    TEST_USER = _config[CURRENT_ENV]["username"]
    TEST_PASSWORD = _config[CURRENT_ENV]["password"]