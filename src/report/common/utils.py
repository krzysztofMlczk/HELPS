def get_metric_from_evaluation_results(evaluation_results, metric_name):
    return [res for res in evaluation_results if res["metric_name"] == metric_name][0]