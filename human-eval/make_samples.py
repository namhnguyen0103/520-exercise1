# make_samples.py
import json, pathlib

pairs = [
    ("HumanEval/100", "gpt-cot/he100.py", "gpt-cot/he100.jsonl"),
    ("HumanEval/100", "gpt-sp/he100.py", "gpt-sp/he100.jsonl"),
    ("HumanEval/100", "gemini-cot/he100.py", "gemini-cot/he100.jsonl"),
    ("HumanEval/100", "gemini-sp/he100.py", "gemini-sp/he100.jsonl"),

    ("HumanEval/90", "gpt-cot/he90.py", "gpt-cot/he90.jsonl"),
    ("HumanEval/90", "gpt-sp/he90.py", "gpt-sp/he90.jsonl"),
    ("HumanEval/90", "gemini-cot/he90.py", "gemini-cot/he90.jsonl"),
    ("HumanEval/90", "gemini-sp/he90.py", "gemini-sp/he90.jsonl"),

    ("HumanEval/80", "gpt-cot/he80.py", "gpt-cot/he80.jsonl"),
    ("HumanEval/80", "gpt-sp/he80.py", "gpt-sp/he80.jsonl"),
    ("HumanEval/80", "gemini-cot/he80.py", "gemini-cot/he80.jsonl"),
    ("HumanEval/80", "gemini-sp/he80.py", "gemini-sp/he80.jsonl"),

    ("HumanEval/70", "gpt-cot/he70.py", "gpt-cot/he70.jsonl"),
    ("HumanEval/70", "gpt-sp/he70.py", "gpt-sp/he70.jsonl"),
    ("HumanEval/70", "gemini-cot/he70.py", "gemini-cot/he70.jsonl"),
    ("HumanEval/70", "gemini-sp/he70.py", "gemini-sp/he70.jsonl"),

    ("HumanEval/60", "gpt-cot/he60.py", "gpt-cot/he60.jsonl"),
    ("HumanEval/60", "gpt-sp/he60.py", "gpt-sp/he60.jsonl"),
    ("HumanEval/60", "gemini-cot/he60.py", "gemini-cot/he60.jsonl"),
    ("HumanEval/60", "gemini-sp/he60.py", "gemini-sp/he60.jsonl"),

    ("HumanEval/50", "gpt-cot/he50.py", "gpt-cot/he50.jsonl"),
    ("HumanEval/50", "gpt-sp/he50.py", "gpt-sp/he50.jsonl"),
    ("HumanEval/50", "gemini-cot/he50.py", "gemini-cot/he50.jsonl"),
    ("HumanEval/50", "gemini-sp/he50.py", "gemini-sp/he50.jsonl"),

    ("HumanEval/40", "gpt-cot/he40.py", "gpt-cot/he40.jsonl"),
    ("HumanEval/40", "gpt-sp/he40.py", "gpt-sp/he40.jsonl"),
    ("HumanEval/40", "gemini-cot/he40.py", "gemini-cot/he40.jsonl"),
    ("HumanEval/40", "gemini-sp/he40.py", "gemini-sp/he40.jsonl"),

    ("HumanEval/30", "gpt-cot/he30.py", "gpt-cot/he30.jsonl"),
    ("HumanEval/30", "gpt-sp/he30.py", "gpt-sp/he30.jsonl"),
    ("HumanEval/30", "gemini-cot/he30.py", "gemini-cot/he30.jsonl"),
    ("HumanEval/30", "gemini-sp/he30.py", "gemini-sp/he30.jsonl"),
]


with open("data/my_samples.jsonl", "w") as f:
    for task_id, file_path, sample_path in pairs:
        with open(sample_path, "w") as s:
          code = pathlib.Path(file_path).read_text().strip("\n")
          s.write(json.dumps({"task_id": task_id, "completion": code}) + "\n")
        code = pathlib.Path(file_path).read_text().strip("\n")
        f.write(json.dumps({"task_id": task_id, "completion": code}) + "\n")
