import uuid
from datetime import datetime

def normalize_finding(tool, title, endpoint, severity, evidence="", tags=None):
    return {
        "id": str(uuid.uuid4()),
        "tool": tool,
        "title": title,
        "endpoint": endpoint,
        "severity": severity,
        "evidence": evidence,
        "tags": tags or [],
        "timestamp": datetime.utcnow().isoformat()
    }
