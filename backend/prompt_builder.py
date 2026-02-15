# prompt_builder.py

def build_prompt(revenue, cogs, opex):
    system_instruction = """
You are FinSight SLM, a specialized financial diagnostic model.
Analyze structured financial data and provide management insights.
Follow strict structured format.
"""

    user_input = f"""
Analyze the following financial data:

Revenue: {revenue}
COGS: {cogs}
Operating Expense: {opex}
"""

    full_prompt = f"""
<|system|>
{system_instruction}
<|user|>
{user_input}
<|assistant|>
"""

    return full_prompt
