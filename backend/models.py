from pydantic import BaseModel

class FinancialData(BaseModel):
    current_assets: float = 0
    current_liabilities: float = 0
    inventory: float = 0
    cash: float = 0
    total_assets: float = 0
    total_equity: float = 0
    total_debt: float = 0
    revenue: float = 0
    net_profit: float = 0
    ebit: float = 0
    interest_expense: float = 0
    receivables: float = 0
    working_capital: float = 0


class RatioOutput(BaseModel):
    liquidity: dict
    solvency: dict
    profitability: dict
    efficiency: dict
