# ==========================================
# financial_calculator.py
# Calculate Financial Ratios
# ==========================================

def calculate_ratios(metrics):

    revenue = metrics["revenue"]
    profit = metrics["profit"]
    liabilities = metrics["liabilities"]
    equity = metrics["equity"]

    profit_margin = (profit / revenue) * 100 if revenue > 0 else 0
    debt_equity_ratio = liabilities / equity if equity > 0 else 0

    return {
        "profit_margin": round(profit_margin, 2),
        "debt_equity_ratio": round(debt_equity_ratio, 2),
    }
