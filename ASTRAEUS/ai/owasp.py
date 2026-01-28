def map_owasp(f):
    name = (f.get("name") or "").lower()

    if "xss" in name:
        return "A03:2021 – Injection"

    if "jwt" in name:
        return "A02:2021 – Broken Authentication"

    if "sql" in name:
        return "A03:2021 – Injection"

    if "auth" in name:
        return "A07:2021 – Identification and Authentication Failures"

    return "A05:2021 – Security Misconfiguration"
