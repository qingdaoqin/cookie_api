import yaml
from pathlib import Path

def read_test_data(yaml_path):
    """读取yaml数据"""
    full_path = Path(__file__).parent / "data" / yaml_path
    with open(full_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f.read())