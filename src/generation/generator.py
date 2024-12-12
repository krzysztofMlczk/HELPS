import json
import os
import tqdm
import time
from datetime import datetime
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()
OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY= os.getenv("ANTHROPIC_API_KEY")

# MODELS:
# GPT-4
# CLAUDE 3.5 Haiku
# GEMINI 2.0

system_prompt = "You are a friendly and knowledgeable assistant, skilled in providing practical advice and support for everyday life. Your role is to help users solve real-life problems, make decisions, and answer questions related to daily activities in a clear, concise, and actionable manner. Ensure your responses are helpful, fact-based, and empathetic. Always clarify uncertainties and avoid guessing if you're unsure about something. Where appropriate, provide step-by-step instructions or examples to support your advice."

# These values were determined based on manual tests conducted for each model
llm_settings = {
    "frequency_penalty": None,# DEFAULTS: openai->0,
    "presence_penalty": None, # DEFAULTS: openai->0,
    # 0.7 to balance coherence and creativity
    "temperature": 0.7, # DEFAULTS: openai->1
    "top_p": None, # DEFAULTS: openai->1
    "n": 1, # DEFAULTS: openai->1
    # Not specified to allow any content length
    "max_tokens": None, # DEFAULTS: openai->None,
}

def load_dataset():
    with open("../dataset/helps.json", "r") as file:
        data = json.load(file)
        return data


def get_llm(model_name):
    match model_name:
        case "gpt-4":
            # During tests points to gpt-4-0613 (Snapshot of gpt-4 from June 13th 2023 with improved function calling support) source: https://platform.openai.com/docs/models/gp#gpt-4-turbo-and-gpt-4
            return ChatOpenAI(
                model="gpt-4",
                api_key=OPEN_AI_API_KEY,
                frequency_penalty=llm_settings["frequency_penalty"],
                presence_penalty=llm_settings["presence_penalty"],
                temperature=llm_settings["temperature"],
                top_p=llm_settings["top_p"],
                max_tokens=llm_settings["max_tokens"],
            )
        case "claude-3-5":
            return ChatAnthropic(
                model="claude-3-5-sonnet-20241022",
                api_key=ANTHROPIC_API_KEY,
                frequency_penalty=llm_settings["frequency_penalty"],
                presence_penalty=llm_settings["presence_penalty"],
                temperature=llm_settings["temperature"],
                top_p=llm_settings["top_p"],
                max_tokens=llm_settings["max_tokens"],
            )
        case _:
            raise Exception("Unsupported model")

def dump_to_file(data, file_name):
    with open(file_name, "a") as file:
        file.write(json.dumps(data, indent=2))

def generate(model_name):
    dataset = load_dataset()
    llm = get_llm(model_name)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt,
            ),
            (
                "human",
                "{user_input}",
            ),
        ]
    )
    results = []
    file_date_prefix = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file_name = f"{file_date_prefix}_log_{model_name}.json"
    results_file_name = f"{file_date_prefix}_results_{model_name}.json"

    for dataset_item in tqdm.tqdm(dataset):
        try:
            chain = prompt | llm
            llm_output = chain.invoke({"user_input": dataset_item["input"]})
            result = {
                **dataset_item,
                "output": llm_output.model_dump()
            }
            results.append(result)
            dump_to_file(result, log_file_name)
            time.sleep(1)
        except Exception as e:
            dump_to_file(str(e), log_file_name)
    dump_to_file(results, results_file_name)


generate("gpt-4")
