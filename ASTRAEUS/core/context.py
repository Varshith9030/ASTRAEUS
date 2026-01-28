class ScanContext:
    def __init__(self, args):
        self.url = args.url
        self.api = args.api
        self.source = args.source
        self.auth = args.auth
        self.ai_enabled = args.ai
        self.findings = []

    def add_findings(self, data):
        self.findings.extend(data)
