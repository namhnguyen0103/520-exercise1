from datasets import load_dataset
import json

ds = load_dataset("codeparrot/apps", split="test", difficulties=["competition"])
problem_id = 100
it = iter(ds)
sample = next(it)
for i in range(problem_id):
    sample = next(it)
# non-empty solutions and input_output features can be parsed from text format this way:
sample["solutions"] = json.loads(sample["solutions"])
sample["input_output"] = json.loads(sample["input_output"])
print(sample["question"])

with open("problems/problem_" + str(problem_id) + ".json", "w", encoding="utf-8") as f:
    json.dump(sample, f, indent=2, ensure_ascii=False)