import json

file_path = "data/resumes_dataset.jsonl"

with open(file_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        resume = json.loads(line)

        print(f"\nResume #{i+1}")
        print("Keys available:", resume.keys())

        # Print some important fields safely
        print("Role:", resume.get("Category", "N/A"))
        print("Summary (snippet):", str(resume.get("summary", ""))[:200])

        print("-" * 60)

        if i == 2:  # only inspect first 3 resumes
            break
3