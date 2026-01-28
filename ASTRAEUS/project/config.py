import yaml
import os

DEFAULT_CONFIG = {
    "ai_profile": {
        "aggressiveness": "medium",
        "false_positive_tolerance": "medium",
        "focus": []
    }
}

def load_project_config(project_dir):
    config_path = os.path.join(project_dir, "config.yaml")

    if not os.path.exists(config_path):
        return DEFAULT_CONFIG

    with open(config_path) as f:
        return yaml.safe_load(f)
