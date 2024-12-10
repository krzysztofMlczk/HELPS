from langchain_openai import OpenAI
from deepeval.models import DeepEvalBaseLLM


class LLama_32_3b_instruct(DeepEvalBaseLLM):
    def __init__(self):
        self.model = "llama-3.2-3b-instruct"
        self.model = client = OpenAI(
            model=self.model,
            base_url="http://localhost:1234/v1",
            api_key="lm-studio",
        )

    def load_model(self):
        return self.model

    def generate(self, prompt: str) -> str:
        return self.load_model().invoke(prompt)

    async def a_generate(self, prompt: str) -> str:
        return self.generate(prompt)

    def get_model_name(self):
        return self.model
