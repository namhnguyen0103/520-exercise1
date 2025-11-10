# make_samples.py
import json, pathlib

pairs = [
    ("HumanEval/100", "gpt_cot/he100.py", "gpt_cot/he100.jsonl"),
    ("HumanEval/100", "gpt_sp/he100.py", "gpt_sp/he100.jsonl"),
    ("HumanEval/100", "gemini_cot/he100.py", "gemini_cot/he100.jsonl"),
    ("HumanEval/100", "gemini_sp/he100.py", "gemini_sp/he100.jsonl"),

    ("HumanEval/90", "gpt_cot/he90.py", "gpt_cot/he90.jsonl"),
    ("HumanEval/90", "gpt_sp/he90.py", "gpt_sp/he90.jsonl"),
    ("HumanEval/90", "gemini_cot/he90.py", "gemini_cot/he90.jsonl"),
    ("HumanEval/90", "gemini_sp/he90.py", "gemini_sp/he90.jsonl"),

    ("HumanEval/80", "gpt_cot/he80.py", "gpt_cot/he80.jsonl"),
    ("HumanEval/80", "gpt_sp/he80.py", "gpt_sp/he80.jsonl"),
    ("HumanEval/80", "gemini_cot/he80.py", "gemini_cot/he80.jsonl"),
    ("HumanEval/80", "gemini_sp/he80.py", "gemini_sp/he80.jsonl"),

    ("HumanEval/70", "gpt_cot/he70.py", "gpt_cot/he70.jsonl"),
    ("HumanEval/70", "gpt_sp/he70.py", "gpt_sp/he70.jsonl"),
    ("HumanEval/70", "gemini_cot/he70.py", "gemini_cot/he70.jsonl"),
    ("HumanEval/70", "gemini_sp/he70.py", "gemini_sp/he70.jsonl"),

    ("HumanEval/60", "gpt_cot/he60.py", "gpt_cot/he60.jsonl"),
    ("HumanEval/60", "gpt_sp/he60.py", "gpt_sp/he60.jsonl"),
    ("HumanEval/60", "gemini_cot/he60.py", "gemini_cot/he60.jsonl"),
    ("HumanEval/60", "gemini_sp/he60.py", "gemini_sp/he60.jsonl"),

    ("HumanEval/50", "gpt_cot/he50.py", "gpt_cot/he50.jsonl"),
    ("HumanEval/50", "gpt_sp/he50.py", "gpt_sp/he50.jsonl"),
    ("HumanEval/50", "gemini_cot/he50.py", "gemini_cot/he50.jsonl"),
    ("HumanEval/50", "gemini_sp/he50.py", "gemini_sp/he50.jsonl"),

    ("HumanEval/40", "gpt_cot/he40.py", "gpt_cot/he40.jsonl"),
    ("HumanEval/40", "gpt_sp/he40.py", "gpt_sp/he40.jsonl"),
    ("HumanEval/40", "gemini_cot/he40.py", "gemini_cot/he40.jsonl"),
    ("HumanEval/40", "gemini_sp/he40.py", "gemini_sp/he40.jsonl"),

    ("HumanEval/30", "gpt_cot/he30.py", "gpt_cot/he30.jsonl"),
    ("HumanEval/30", "gpt_sp/he30.py", "gpt_sp/he30.jsonl"),
    ("HumanEval/30", "gemini_cot/he30.py", "gemini_cot/he30.jsonl"),
    ("HumanEval/30", "gemini_sp/he30.py", "gemini_sp/he30.jsonl"),
]


with open("data/my_samples.jsonl", "w") as f:
    for task_id, file_path, sample_path in pairs:
        with open(sample_path, "w") as s:
          code = pathlib.Path(file_path).read_text().strip("\n")
          s.write(json.dumps({"task_id": task_id, "completion": code}) + "\n")
        code = pathlib.Path(file_path).read_text().strip("\n")
        f.write(json.dumps({"task_id": task_id, "completion": code}) + "\n")
