from src.report.common.load_evaluation_data import load_evaluation_data
from src.report.common.utils import get_metric_from_evaluation_results

weights = {"helpfulness": 0.5, "relevancy": 0.3, "brevity": 0.2}

evaluation_data = load_evaluation_data()


def calculate_overall_score(model_name):
    data = evaluation_data[model_name]

    weighted_sum = 0

    for task in data:
        eval_results = task["evaluation"]["results"]
        helpfulness_score = get_metric_from_evaluation_results(
            eval_results, "helpfulness"
        )["score"]
        relevancy_score = get_metric_from_evaluation_results(eval_results, "relevancy")[
            "score"
        ]
        brevity_score = get_metric_from_evaluation_results(eval_results, "brevity")[
            "score"
        ]
        task_weighted_score = (
            weights["helpfulness"] * helpfulness_score
            + weights["relevancy"] * relevancy_score
            + weights["brevity"] * brevity_score
        )
        weighted_sum += task_weighted_score

    return weighted_sum / len(data)


def get_overall_scores():
    overall_scores = {
        "gpt-4": calculate_overall_score("gpt-4"),
        "gemini-1-5-pro": calculate_overall_score("gemini-1-5-pro"),
        "claude-3-5-sonnet": calculate_overall_score("claude-3-5-sonnet"),
    }
    return overall_scores