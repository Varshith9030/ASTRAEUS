from project.manager import ProjectManager
from plugins.nuclei_plugin import NucleiPlugin
from plugins.osv_plugin import OSVPlugin
from ai.analyzer import analyze_findings
from storage.diff import diff_scans
from reporting.pdf_report import generate_pdf

PLUGINS = [
    NucleiPlugin(),
    OSVPlugin()
]

def run_scan(args):
    project = ProjectManager(args.project)
    findings = []

    for plugin in PLUGINS:
        findings.extend(
            plugin.run(args.url or args.source, args.auth, project.config)
        )

    analyzed = analyze_findings(findings, project.config["ai_profile"])

    last_scan = project.load_last_scan()
    if last_scan:
        diff = diff_scans(last_scan, analyzed)
        print("[+] Scan diff:", diff)

    project.save_scan(analyzed)

    if args.output.endswith(".pdf"):
        generate_pdf(analyzed, args.output)
