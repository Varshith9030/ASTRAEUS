def load_bearer(path):
    if not path:
        return None
    with open(path, "r") as f:
        return f.read().strip()
