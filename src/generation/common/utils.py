import json
from datetime import datetime

def dump_to_file(data, file_name):
    with open(file_name, "a") as file:
        file.write(json.dumps(data, indent=2))


def get_results_file_name(model_name):
    return f"./results/{get_file_date_prefix()}_results_{model_name}.json"


def get_log_file_name(model_name):
    return f"./logs/{get_file_date_prefix()}_log_{model_name}.json"


def get_file_date_prefix():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def load_dataset():
    with open("../../dataset/helps.json", "r") as file:
        data = json.load(file)
        return data


def get_system_prompt():
    with open("../common/system_prompt.txt", "r") as file:
        system_prompt = file.read()
        return system_prompt
