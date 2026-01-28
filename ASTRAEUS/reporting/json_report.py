import json

def generate_json(findings, output):
    with open(output, "w") as f:
        json.dump(findings, f, indent=2)
