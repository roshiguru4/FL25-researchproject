import subprocess, tempfile, json

def validate_snippet(snippet):
    code = snippet["code"]

    lines = code.strip().split("\n")
    if not (5 <= len(lines) <= 12):
        return False

    try:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write(code)
            f.flush()
            result = subprocess.run(
                ["python3", f.name],
                capture_output=True,
                timeout=1
            )
        if snippet.get("buggy") is False and result.returncode != 0:
            return False
    except Exception:
        return False

    return True
