import tqdm
import requests
import os

from dotenv import load_dotenv

from src.generation.common.utils import (
    load_dataset,
    get_system_prompt,
    get_log_file_name,
    get_results_file_name,
    dump_to_file,
)

load_dotenv()
FAB_STUDIO_API_KEY = os.getenv("FAB_STUDIO_API_KEY")
FAB_AGENT_WORKSPACE_ID_HEADER = os.getenv("FAB_AGENT_WORKSPACE_ID_HEADER")
FAB_AGENT_USER_ID_HEADER = os.getenv("FAB_AGENT_USER_ID_HEADER")
FAB_AGENT_LAMBDA_URL = os.getenv("FAB_AGENT_LAMBDA_URL")


def generate(model_name, limit=None):
    dataset = load_dataset()[:limit]
    results = []
    log_file_name = get_log_file_name(model_name)
    results_file_name = get_results_file_name(model_name)

    for dataset_item in tqdm.tqdm(dataset):
        try:
            response = requests.post(
                FAB_AGENT_LAMBDA_URL,
                headers={
                    "Content-Type": "application/json",
                    "x-workspace-id": FAB_AGENT_WORKSPACE_ID_HEADER,
                    "x-user-id": FAB_AGENT_USER_ID_HEADER,
                    "x-authentication": f"api-key {FAB_STUDIO_API_KEY}",
                },
                json={
                    "input": {
                        "system_prompt": get_system_prompt(),
                        "user_prompt": dataset_item["input"],
                    }
                },
            )
            result = {**dataset_item, "output": response.json()}
            results.append(result)
            dump_to_file(result, log_file_name)
        except Exception as e:
            dump_to_file(str(e), log_file_name)
            print(str(e))
    dump_to_file(results, results_file_name)


generate("gpt-4")
