import json
from gpt.wrapper import GPTWrapper

llm = GPTWrapper(model="gpt-4.1")

def generate_snippet(topic, difficulty, buggy=False):
    prompt = f"""
    Create a Python coding problem. Output JSON with keys:
    - "problem": short description for a participant
    - "code": a 5–12 line Python code snippet
    - "difficulty": "{difficulty}"
    - "buggy": {str(buggy).lower()}

    Requirements:
    - Topic: {topic}
    - If buggy=true: insert ONE logical bug (not syntax).
    - If buggy=false: code MUST run correctly.
    - Code must be self-contained, no imports except built-ins.

    JSON ONLY.
    """
    raw = llm.structured(prompt)
    return json.loads(raw)

