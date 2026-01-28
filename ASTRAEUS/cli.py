import argparse
from core.runner import run_scan

def main():
    parser = argparse.ArgumentParser(
        description="ASTRAEUS – AI Penetration Testing Tool (Phase 2)"
    )

    # 🔥 PHASE 2 REQUIRED
    parser.add_argument(
        "--project",
        required=True,
        help="Project name (used for history, config, diffing)"
    )

    # Targets
    parser.add_argument("--url", help="Target URL")
    parser.add_argument("--api", help="OpenAPI / Swagger file")
    parser.add_argument("--source", help="Source code directory")

    # Auth
    parser.add_argument("--auth", help="Bearer token file")

    # AI + Output
    parser.add_argument("--ai", action="store_true", help="Enable AI analysis")
    parser.add_argument("--output", default="report.json", help="Output file")
    parser.add_argument("--json", action="store_true", help="JSON output")

    args = parser.parse_args()
    run_scan(args)
