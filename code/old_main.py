# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

SYSTEM_PROMPT = """
You are a language model tasked with judging whether two statements convey the same logical meaning. In each case:

1. Carefully analyze each sentence for logical structure, core concepts, and relationships between components.
2. Identify if any changes in wording alter the logical meaning or intent of the statements.
3. Ignore superficial differences, such as synonym substitutions, rephrasing, or grammatical adjustments that do not change the underlying logic.
4. Consider sentences logically equivalent only if they express the same relationships, outcomes, and implications in all scenarios.
Your task is to answer 'Yes' if the sentences have the same logical meaning or 'No' if they do not. Provide a brief explanation for your decision based on logical similarities or differences.
"""

completion = client.chat.completions.create(
    model="llama-3.2-3b-instruct",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user",
         "content": "statement 1: 'ala jest właścicielem kota'; statement 2: 'kot ma właściciela - alę'"},
    ],
    temperature=0.0,
)

print(completion.choices[0].message)
