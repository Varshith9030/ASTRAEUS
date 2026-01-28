import os
import json
from datetime import datetime
from project.config import load_project_config

BASE_DIR = os.path.expanduser("~/.astraeus/projects")

class ProjectManager:
    def __init__(self, name):
        self.name = name
        self.project_dir = os.path.join(BASE_DIR, name)
        self.scan_dir = os.path.join(self.project_dir, "scans")
        os.makedirs(self.scan_dir, exist_ok=True)

        self.config = load_project_config(self.project_dir)

    def save_scan(self, findings):
        scan_id = datetime.now().strftime("%Y-%m-%d_%H-%M")
        path = os.path.join(self.scan_dir, f"{scan_id}.json")

        with open(path, "w") as f:
            json.dump(findings, f, indent=2)

        return scan_id, path

    def load_last_scan(self):
        scans = sorted(os.listdir(self.scan_dir))
        if len(scans) < 2:
            return None

        with open(os.path.join(self.scan_dir, scans[-2])) as f:
            return json.load(f)
