import json
from utils.exec import run_cmd

def run_osv(source_dir):
    cmd = f"osv-scanner scan --json {source_dir}"
    output = run_cmd(cmd)
    try:
        return json.loads(output)
    except:
        return []
