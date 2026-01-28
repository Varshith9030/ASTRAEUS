import json
from utils.exec import run_cmd
from plugins.base import ScannerPlugin
from schemas.finding import normalize_finding

class NucleiPlugin(ScannerPlugin):
    name = "nuclei"

    def run(self, target, auth, config):
        cmd = f"nuclei -u {target} -json"
        if auth:
            cmd += f" -H 'Authorization: Bearer {auth}'"

        output = run_cmd(cmd)
        findings = []

        for line in output.splitlines():
            try:
                data = json.loads(line)
                findings.append(
                    normalize_finding(
                        tool="nuclei",
                        title=data.get("info", {}).get("name"),
                        endpoint=data.get("matched-at"),
                        severity=data.get("info", {}).get("severity", "low"),
                        evidence=data.get("matcher-name"),
                        tags=data.get("info", {}).get("tags", [])
                    )
                )
            except:
                continue

        return findings
