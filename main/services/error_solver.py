from main.models.groq_model import load_llm
from main.prompts.error import error_solver_prompt

llm = load_llm()

def solve_error(user_input):
    prompt =error_solver_prompt(user_input)

    result = llm.invoke(prompt)
    return result.content