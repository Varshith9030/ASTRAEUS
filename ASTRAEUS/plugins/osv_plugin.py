import json
from utils.exec import run_cmd
from plugins.base import ScannerPlugin
from schemas.finding import normalize_finding

class OSVPlugin(ScannerPlugin):
    name = "osv"

    def run(self, target, auth, config):
        cmd = f"osv-scanner scan --json {target}"
        output = run_cmd(cmd)

        try:
            data = json.loads(output)
        except:
            return []

        findings = []
        for vuln in data.get("vulnerabilities", []):
            findings.append(
                normalize_finding(
                    tool="osv",
                    title=vuln.get("id"),
                    endpoint=vuln.get("package", {}).get("name"),
                    severity="high",
                    evidence=vuln.get("summary"),
                    tags=["dependency"]
                )
            )
        return findings
