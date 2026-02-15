from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
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


@app.post("/analyze_pdf")
async def analyze_pdf(file: UploadFile = File(...)):

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Step 1: Extract
    financial_data = extract_financial_data(file_path)

    # Step 2: Calculate Ratios
    ratios = calculate_ratios(financial_data)

    # Step 3: Interpret using SLM
    liquidity_output = generate_response(
        build_prompt("Liquidity", ratios["liquidity"])
    )

    solvency_output = generate_response(
        build_prompt("Solvency", ratios["solvency"])
    )

    profitability_output = generate_response(
        build_prompt("Profitability", ratios["profitability"])
    )

    efficiency_output = generate_response(
        build_prompt("Efficiency", ratios["efficiency"])
    )

    os.remove(file_path)

    return {
        "extracted_data": financial_data,
        "calculated_ratios": ratios,
        "slm_interpretation": {
            "liquidity": liquidity_output,
            "solvency": solvency_output,
            "profitability": profitability_output,
            "efficiency": efficiency_output
        }
    }
