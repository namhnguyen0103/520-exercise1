import json
import subprocess
import os

def main():
    print("=== Python Solution Tester ===\n")

    # Let user choose solution.py
    solution_path = input("Enter path to your solution file (e.g. solution.py): ").strip()
    while not os.path.exists(solution_path):
        print("❌ File not found. Try again.")
        solution_path = input("Enter path to your solution file: ").strip()

    # Let user choose dataset JSON
    json_path = input("Enter path to JSON dataset (e.g. sample_train_test.json): ").strip()
    while not os.path.exists(json_path):
        print("❌ File not found. Try again.")
        json_path = input("Enter path to JSON dataset: ").strip()

    # Load dataset
    with open(json_path, "r") as f:
        data = json.load(f)

    inputs = data["input_output"]["inputs"]
    outputs = [o.strip() for o in data["input_output"]["outputs"]]

    print(f"\n📘 Loaded {len(inputs)} test cases.")
    print(f"🔧 Testing {solution_path}...\n")

    passed = 0
    total = len(inputs)

    for i, (inp, expected) in enumerate(zip(inputs, outputs), start=1):
        try:
            # Run solution.py using subprocess
            result = subprocess.run(
                ["python3", solution_path],
                input=inp.encode(),
                capture_output=True,
                timeout=2
            )
            actual = result.stdout.decode().strip()

            if actual == expected:
                passed += 1
            else:
                print(f"❌ Test {i} failed:")
                print(f"Input:\n{inp.strip()}")
                print(f"Expected: {expected}")
                print(f"Got:      {actual}\n")

        except subprocess.TimeoutExpired:
            print(f"⚠️ Test {i} timed out.\n")

    print(f"\n✅ Passed {passed}/{total} tests.")
    print(f"📄 Solution: {os.path.basename(solution_path)}")
    print(f"🧪 Dataset:  {os.path.basename(json_path)}\n")


if __name__ == "__main__":
    main()

# import json
# import subprocess
# import os
# import math

# def run_solution(solution_path, inputs, outputs):
#     passed = 0
#     for i, (inp, expected) in enumerate(zip(inputs, outputs), start=1):
#         try:
#             result = subprocess.run(
#                 ["python3", solution_path],
#                 input=inp.encode(),
#                 capture_output=True,
#                 timeout=2
#             )
#             actual = result.stdout.decode().strip()
#             if actual == expected:
#                 passed += 1
#         except subprocess.TimeoutExpired:
#             pass
#     return passed


# def compute_pass_at_k(num_correct, num_total, k):
#     """
#     Standard unbiased estimator for pass@k:
#     pass@k = 1 - comb(num_total - num_correct, k) / comb(num_total, k)
#     """
#     if num_correct == 0:
#         return 0.0
#     if num_total == 0 or k == 0:
#         return 0.0
#     if num_correct > num_total:
#         num_correct = num_total
#     if k > num_total:
#         k = num_total
#     try:
#         return 1.0 - math.comb(num_total - num_correct, k) / math.comb(num_total, k)
#     except ValueError:
#         return 0.0


# def main():
#     print("=== Multi-Solution Tester with pass@k ===\n")

#     # Load dataset JSON
#     json_path = input("Enter path to JSON dataset: ").strip()
#     while not os.path.exists(json_path):
#         print("❌ File not found. Try again.")
#         json_path = input("Enter path to JSON dataset: ").strip()

#     with open(json_path, "r") as f:
#         data = json.load(f)
#     inputs = data["input_output"]["inputs"]
#     outputs = [o.strip() for o in data["input_output"]["outputs"]]
#     total_tests = len(inputs)
#     print(f"📘 Loaded {total_tests} test cases.\n")

#     # Choose solution files
#     print("Enter solution file paths (comma-separated):")
#     solution_files = input("Example: sol1.py, sol2.py → ").strip().split(",")
#     solution_files = [s.strip() for s in solution_files if s.strip()]
#     print()

#     if not solution_files:
#         print("❌ No solution files given.")
#         return

#     results = {}
#     for sol in solution_files:
#         if not os.path.exists(sol):
#             print(f"⚠️ {sol} not found, skipping.")
#             continue
#         print(f"🔧 Testing {sol} ...")
#         passed = run_solution(sol, inputs, outputs)
#         acc = passed / total_tests
#         results[sol] = (passed, acc)
#         print(f"✅ {passed}/{total_tests} tests passed ({acc:.2%})\n")

#     # pass@k summary
#     num_total = len(solution_files)
#     num_correct = sum(1 for _, (p, _) in results.items() if p == total_tests)

#     print("=== Summary ===")
#     for sol, (p, acc) in results.items():
#         print(f"{sol}: {p}/{total_tests} passed ({acc:.2%})")

#     print("\n=== pass@k ===")
#     for k in [1, 2, 3]:
#         if k <= num_total:
#             p = compute_pass_at_k(num_correct, num_total, k)
#             print(f"pass@{k}: {p:.4f}")
#     print()


# if __name__ == "__main__":
#     main()

