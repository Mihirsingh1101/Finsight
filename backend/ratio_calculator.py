def safe_div(a, b):
    return round(a / b, 2) if b != 0 else 0


def calculate_ratios(data):

    ratios = {}

    # -------- LIQUIDITY --------
    ratios["liquidity"] = {
        "Current Ratio": safe_div(
            data.get("current_assets", 0),
            data.get("current_liabilities", 0)
        ),
        "Quick Ratio": safe_div(
            data.get("current_assets", 0) - data.get("inventory", 0),
            data.get("current_liabilities", 0)
        ),
        "Cash Ratio": safe_div(
            data.get("cash", 0),
            data.get("current_liabilities", 0)
        )
    }

    # -------- SOLVENCY --------
    ratios["solvency"] = {
        "Debt to Equity": safe_div(
            data.get("total_debt", 0),
            data.get("total_equity", 0)
        ),
        "Debt Ratio": safe_div(
            data.get("total_debt", 0),
            data.get("total_assets", 0)
        ),
        "Interest Coverage Ratio": safe_div(
            data.get("ebit", 0),
            data.get("interest_expense", 0)
        )
    }

    # -------- PROFITABILITY --------
    ratios["profitability"] = {
        "Net Profit Margin": safe_div(
            data.get("net_profit", 0),
            data.get("revenue", 0)
        ) * 100,
        "ROE": safe_div(
            data.get("net_profit", 0),
            data.get("total_equity", 0)
        ) * 100,
        "ROCE": safe_div(
            data.get("ebit", 0),
            data.get("total_assets", 0)
        ) * 100
    }

    # -------- EFFICIENCY --------
    ratios["efficiency"] = {
        "Inventory Turnover": safe_div(
            data.get("revenue", 0),
            data.get("inventory", 0)
        ),
        "Receivables Turnover": safe_div(
            data.get("revenue", 0),
            data.get("receivables", 0)
        ),
        "Working Capital Turnover": safe_div(
            data.get("revenue", 0),
            data.get("working_capital", 0)
        )
    }

    return ratios
