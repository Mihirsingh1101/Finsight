# main.py

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

from pdf_extractor import extract_financial_data
from ratio_calculator import calculate_ratios
from slm_interpreter import build_prompt, generate_response


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# MANUAL INPUT MODEL
# ==========================================
class FinancialInput(BaseModel):
    current_assets: float = 0
    current_liabilities: float = 0
    inventory: float = 0
    cash: float = 0
    total_assets: float = 0
    total_equity: float = 0
    revenue: float = 0
    net_profit: float = 0
    ebit: float = 0
    interest_expense: float = 0
    receivables: float = 0
    total_debt: float = 0


# ==========================================
# PDF ANALYZER
# ==========================================
@app.post("/analyze_pdf")
async def analyze_pdf(file: UploadFile = File(...)):

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # 1️⃣ Extract
    financial_data = extract_financial_data(file_path)

    # 2️⃣ Calculate
    ratios = calculate_ratios(financial_data)

    # 3️⃣ Interpret
    slm_outputs = {}

    for category in ratios:
        slm_outputs[category] = generate_response(
            build_prompt(category.capitalize(), ratios[category]),
            ratios[category]
        )

    os.remove(file_path)

    return {
        "extracted_data": financial_data,
        "calculated_ratios": ratios,
        "slm_interpretation": slm_outputs
    }


# ==========================================
# MANUAL ANALYZER
# ==========================================
@app.post("/analyze_manual")
async def analyze_manual(data: FinancialInput):

    financial_data = data.dict()

    # 1️⃣ Calculate
    ratios = calculate_ratios(financial_data)

    # 2️⃣ Interpret
    slm_outputs = {}

    for category in ratios:
        slm_outputs[category] = generate_response(
            build_prompt(category.capitalize(), ratios[category]),
            ratios[category]
        )

    return {
        "extracted_data": financial_data,
        "calculated_ratios": ratios,
        "slm_interpretation": slm_outputs
    }
