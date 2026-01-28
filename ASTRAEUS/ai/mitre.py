def map_mitre(f):
    name = (f.get("name") or "").lower()

    if "xss" in name:
        return ["T1059.007 - JavaScript"]

    if "jwt" in name:
        return ["T1552.004 - Credentials in Tokens"]

    if "sql" in name:
        return ["T1190 - Exploit Public-Facing Application"]

    if "auth" in name:
        return ["T1078 - Valid Accounts"]

    return ["T1190 - Exploit Application"]
