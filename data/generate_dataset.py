import random
import json

SYSTEM_PROMPT = """You are FinSight SLM, a financial ratio interpretation specialist.

You receive a financial category and ratio values.

You must:
- Provide one-line interpretation per ratio.
- Provide 2–3 line category summary.
- Do NOT generate tables.
- Do NOT calculate.
- Do NOT invent ratios.
- Only interpret given values.
- Keep response concise and structured.
"""

def interpret_current_ratio(value):
    if value < 1:
        return "Indicates potential short-term liquidity stress."
    elif value < 1.5:
        return "Suggests limited short-term solvency cushion."
    elif value < 3:
        return "Reflects healthy short-term liquidity position."
    else:
        return "May indicate excess idle current assets."

def interpret_de_ratio(value):
    if value < 0.5:
        return "Indicates conservative leverage structure."
    elif value < 1:
        return "Shows balanced capital structure."
    elif value < 2:
        return "Suggests elevated reliance on debt financing."
    else:
        return "Indicates heavy financial leverage and risk."

def interpret_profit_margin(value):
    if value < 0:
        return "Indicates operating losses."
    elif value < 5:
        return "Shows weak profitability."
    elif value < 15:
        return "Reflects moderate profit generation."
    else:
        return "Demonstrates strong profitability."

def interpret_turnover(value):
    if value < 2:
        return "Indicates inefficient asset utilization."
    elif value < 5:
        return "Shows moderate operational efficiency."
    else:
        return "Reflects strong operational efficiency."

def generate_liquidity():
    cr = round(random.uniform(0.3, 5.0), 2)
    qr = round(random.uniform(0.2, 4.5), 2)
    cash = round(random.uniform(0.1, 3.0), 2)

    user = f"""Category: Liquidity

Current Ratio: {cr}
Quick Ratio: {qr}
Cash Ratio: {cash}
"""

    assistant = f"""LIQUIDITY ANALYSIS

Current Ratio: {cr}
→ {interpret_current_ratio(cr)}

Quick Ratio: {qr}
→ {interpret_current_ratio(qr)}

Cash Ratio: {cash}
→ {interpret_current_ratio(cash)}

Liquidity Summary:
Overall liquidity position reflects short-term solvency conditions based on asset coverage of liabilities.
"""

    return user, assistant

def generate_solvency():
    de = round(random.uniform(0.1, 3.5), 2)
    dr = round(random.uniform(0.1, 0.9), 2)
    icr = round(random.uniform(0.5, 8.0), 2)

    user = f"""Category: Solvency

Debt to Equity: {de}
Debt Ratio: {dr}
Interest Coverage Ratio: {icr}
"""

    assistant = f"""SOLVENCY ANALYSIS

Debt to Equity: {de}
→ {interpret_de_ratio(de)}

Debt Ratio: {dr}
→ {interpret_de_ratio(dr)}

Interest Coverage Ratio: {icr}
→ {interpret_de_ratio(icr)}

Solvency Summary:
Leverage levels indicate the company’s long-term financial risk exposure.
"""

    return user, assistant

def generate_profitability():
    margin = round(random.uniform(-10, 30), 2)
    roe = round(random.uniform(-5, 35), 2)
    roce = round(random.uniform(-5, 30), 2)

    user = f"""Category: Profitability

Net Profit Margin: {margin}%
ROE: {roe}%
ROCE: {roce}%
"""

    assistant = f"""PROFITABILITY ANALYSIS

Net Profit Margin: {margin}%
→ {interpret_profit_margin(margin)}

ROE: {roe}%
→ {interpret_profit_margin(roe)}

ROCE: {roce}%
→ {interpret_profit_margin(roce)}

Profitability Summary:
Profitability metrics indicate overall earnings efficiency and shareholder return performance.
"""

    return user, assistant

def generate_efficiency():
    inv = round(random.uniform(0.5, 10), 2)
    rec = round(random.uniform(0.5, 10), 2)
    wc = round(random.uniform(0.5, 8), 2)

    user = f"""Category: Efficiency

Inventory Turnover: {inv}
Receivables Turnover: {rec}
Working Capital Turnover: {wc}
"""

    assistant = f"""EFFICIENCY ANALYSIS

Inventory Turnover: {inv}
→ {interpret_turnover(inv)}

Receivables Turnover: {rec}
→ {interpret_turnover(rec)}

Working Capital Turnover: {wc}
→ {interpret_turnover(wc)}

Efficiency Summary:
Operational efficiency reflects how effectively assets are utilized to generate revenue.
"""

    return user, assistant

def generate_dataset(num_samples=1000):
    data = []
    generators = [generate_liquidity, generate_solvency, generate_profitability, generate_efficiency]

    for _ in range(num_samples):
        gen = random.choice(generators)
        user, assistant = gen()

        data.append({
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user},
                {"role": "assistant", "content": assistant}
            ]
        })

    with open("training_data.jsonl", "w") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")

generate_dataset(1000)
print("Dataset generated: training_data.jsonl")
