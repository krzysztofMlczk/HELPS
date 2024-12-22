import numpy as np
from src.report.common.load_evaluation_data import load_evaluation_data
from src.report.common.utils import get_metric_from_evaluation_results

evaluation_data = load_evaluation_data()

def calc(arr, kind):
    match kind:
        case "avg":
            return np.mean(arr)

def calculate_for_metric(model_name, metric_name, kind="avg"):
    data = evaluation_data[model_name]

    metric_scores = []

    for task in data:
        eval_results = task["evaluation"]["results"]
        metric_score = get_metric_from_evaluation_results(
            eval_results, metric_name
        )["score"]
        metric_scores.append(metric_score)

    return calc(metric_scores, kind)