from human_eval.data import write_jsonl, read_problems

problems = read_problems()

problem = "30"
problems_id = ["100", "90", "80", "70", "60", "50", "40", "30"]

samples = [
    problems["HumanEval/" + id]
    for id in problems_id
]
write_jsonl("problem/all_problems.jsonl", samples)
write_jsonl("problem/he" + problem + ".jsonl", [problems["HumanEval/" + problem]])
print(problems["HumanEval/" + problem]["prompt"])