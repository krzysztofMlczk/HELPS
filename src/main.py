# IDEAS:
# for each provider write class
# each of these classes should follow the same interface
# and have at least one public method for actually calling the model with:
# MODEL, SYSTEM_PROMPT, TEMPERATURE (and whatever else that seems to make sense)
from deepeval.test_case import LLMTestCase

from deepeval.metrics import AnswerRelevancyMetric

from src.custom_llm_evaluators.hf_transformers.mistral_7b import CustomMistral7B
from src.custom_llm_evaluators.lm_studio.llama_32_3b_instruct import LLama_32_3b_instruct

llama = LLama_32_3b_instruct()
mistral = CustomMistral7B()


metric = AnswerRelevancyMetric(model=mistral)
prompt = "What are you?"
generated = llama.generate(prompt)
score = metric.measure(
    LLMTestCase(input=prompt, actual_output=generated)
)
print(score)

