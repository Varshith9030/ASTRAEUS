import json
from utils.exec import run_cmd

def run_nuclei(url, token):
    cmd = f"nuclei -u {url} -json"
    if token:
        cmd += f" -H 'Authorization: Bearer {token}'"

    output = run_cmd(cmd)
    findings = []

    for line in output.splitlines():
        try:
            findings.append(json.loads(line))
        except:
            pass

    return findings
