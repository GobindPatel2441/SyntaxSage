from main.models.groq_model import load_llm
from main.prompts.code_prompt import code_generator_prompt

llm = load_llm()

def generate_code(user_input):
    prompt= code_generator_prompt(user_input)
    result = llm.invoke(prompt)
    return result.content