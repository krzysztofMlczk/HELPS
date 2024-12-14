import os
import json
import tqdm
from datetime import datetime

from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from deepeval.models.base_model import DeepEvalBaseLLM

load_dotenv()
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_GPT4o_DEPLOYMENT = os.getenv("AZURE_OPENAI_GPT4o_DEPLOYMENT")
AZURE_OPENAI_GPT4o_MODEL = os.getenv("AZURE_OPENAI_GPT4o_MODEL")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")


class AzureOpenAIGpt4o(DeepEvalBaseLLM):
    def __init__(self):
        self.model = AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            azure_deployment=AZURE_OPENAI_GPT4o_DEPLOYMENT,
            model=AZURE_OPENAI_GPT4o_MODEL,
            api_version=AZURE_OPENAI_API_VERSION,
            cache=False,
        )

    def load_model(self):
        return self.model

    def generate(self, prompt: str) -> str:
        chat_model = self.load_model()
        res = chat_model.invoke(prompt)
        return res.content

    async def a_generate(self, prompt: str) -> str:
        chat_model = self.load_model()
        res = await chat_model.ainvoke(prompt)
        return res.content

    def get_model_name(self):
        return "gpt-4o(azure)"


azure_openai_gpt4o_model = AzureOpenAIGpt4o()


def get_file_date_prefix():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def get_log_file_name(model_name):
    return f"./logs/{get_file_date_prefix()}_log_{model_name}.json"


def get_results_file_name(model_name):
    return f"./results/{get_file_date_prefix()}_results_{model_name}.json"


def dump_to_file(data, file_name):
    with open(file_name, "a") as file:
        file.write(json.dumps(data, indent=2))


def load_generation_results(file_name):
    with open(f"../../generation/with_agents/results/{file_name}", "r") as file:
        data = json.load(file)
        return data


def run_evaluation(generation_results_per_model, metrics: list[GEval], limit=None):
    for entry in tqdm.tqdm(generation_results_per_model):
        model_name = entry["model_name"]
        file_name = entry["file_name"]

        generation_results = load_generation_results(file_name)[:limit]

        evaluation_results = []
        log_file_name = get_log_file_name(model_name)
        results_file_name = get_results_file_name(model_name)

        for generation_result in tqdm.tqdm(generation_results):
            evaluation_result = {**generation_result, "evaluation": {"results": []}}
            test_input = generation_result["input"]
            test_actual_output = generation_result["output"]["output"]["content"][
                "content"
            ]
            test_case = LLMTestCase(input=test_input, actual_output=test_actual_output)
            for metric in tqdm.tqdm(metrics):
                metric.measure(test_case)
                evaluation_result["evaluation"]["results"].append(
                    {
                        "metric_name": metric.name,
                        "score": metric.score,
                        "reason": metric.reason,
                        "criteria": metric.criteria,
                        "evaluation_steps": metric.evaluation_steps,
                        "evaluation_model": metric.evaluation_model,
                        "verbose_logs": metric.verbose_logs,
                    }
                )
            evaluation_results.append(evaluation_result)
            dump_to_file(evaluation_result, log_file_name)
        dump_to_file(evaluation_results, results_file_name)


run_evaluation(
    [
        {
            "model_name": "gpt-4",
            "file_name": "2024-12-13_22-46-23_results_gpt-4.json",
        },
        {
            "model_name": "gemini-1-5-pro",
            "file_name": "2024-12-13_23-34-06_results_gemini-1-5-pro.json",
        },
        {
            "model_name": "claude-3-5-sonnet",
            "file_name": "2024-12-14_00-00-23_results_claude-3-5-sonnet.json",
        },
    ],
    [
        GEval(
            name="brevity",
            criteria="Determine the brevity of the actual output in the context of input",
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
            model=azure_openai_gpt4o_model,
            verbose_mode=True,
        ),
        GEval(
            name="relevancy",
            criteria="Determine the relevancy of the actual output in the context of input",
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
            model=azure_openai_gpt4o_model,
            verbose_mode=True,
        ),
        GEval(
            name="helpfulness",
            criteria="Determine the helpfulness of the actual output in the context of input",
            evaluation_params=[
                LLMTestCaseParams.INPUT,
                LLMTestCaseParams.ACTUAL_OUTPUT,
            ],
            model=azure_openai_gpt4o_model,
            verbose_mode=True,
        ),
    ],
)
