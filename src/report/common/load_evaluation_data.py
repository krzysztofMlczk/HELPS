import json

def load_evaluation_results(file_name):
    with open(f"../../evaluation/with-agents/results/{file_name}") as file:
        return json.load(file)

def load_evaluation_data():
    evaluation_data = {
        "gpt-4": load_evaluation_results("2024-12-14_16-04-06_results_gpt-4.json"),
        "gemini-1-5-pro": load_evaluation_results(
            "2024-12-14_16-11-57_results_gemini-1-5-pro.json"
        ),
        "claude-3-5-sonnet": load_evaluation_results(
            "2024-12-14_16-19-42_results_claude-3-5-sonnet.json"
        ),
    }
    return evaluation_data