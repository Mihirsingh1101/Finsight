import pdfplumber
import re


LABEL_MAP = {
    "revenue": ["revenue from operations", "total revenue", "net sales", "turnover"],
    "net_profit": ["profit for the period", "net profit", "profit after tax"],
    "ebit": ["profit before tax"],
    "interest_expense": ["finance costs", "interest expense"],
    "current_assets": ["total current assets"],
    "current_liabilities": ["total current liabilities"],
    "inventory": ["inventories"],
    "cash": ["cash and cash equivalents", "cash and bank balances"],
    "total_assets": ["total assets"],
    "total_equity": ["total equity", "shareholders' funds"],
    "receivables": ["trade receivables"]
}


def clean_number(value):
    try:
        return float(str(value).replace(",", "").strip())
    except:
        return 0.0


def extract_candidate_numbers(line):
    nums = re.findall(r'[\d,]+\.?\d*', line)
    cleaned = [clean_number(n) for n in nums]

    # Remove note numbers (small integers)
    cleaned = [n for n in cleaned if n > 50]

    return cleaned


def extract_value_by_labels(text, labels):
    lines = text.split("\n")

    for line in lines:
        for label in labels:
            if label.lower() in line.lower():

                candidates = extract_candidate_numbers(line)

                if candidates:
                    # Choose second largest (usually current year)
                    candidates.sort(reverse=True)
                    return candidates[0]

    return 0.0


def extract_financial_data(pdf_path):

    data = {
        "current_assets": 0.0,
        "current_liabilities": 0.0,
        "inventory": 0.0,
        "cash": 0.0,
        "total_assets": 0.0,
        "total_equity": 0.0,
        "revenue": 0.0,
        "net_profit": 0.0,
        "ebit": 0.0,
        "interest_expense": 0.0,
        "receivables": 0.0,
        "total_debt": 0.0,
        "working_capital": 0.0
    }

    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

    for key, labels in LABEL_MAP.items():
        data[key] = extract_value_by_labels(full_text, labels)

    # Derived
    data["total_debt"] = data["total_assets"] - data["total_equity"]
    data["working_capital"] = data["current_assets"] - data["current_liabilities"]

    return data
