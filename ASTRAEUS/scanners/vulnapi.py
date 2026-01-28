from utils.exec import run_cmd

def run_vulnapi(openapi_file, token):
    cmd = f"vulnapi scan {openapi_file}"
    if token:
        cmd += f" --header 'Authorization: Bearer {token}'"

    output = run_cmd(cmd)
    return [{"tool": "vulnapi", "output": output}]
