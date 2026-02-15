# slm_interpreter.py

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_ID = "Mihirsingh1101/smolified-finsight-ratio-interpreter"

tokenizer = None
model = None


# ---------------------------
# LOAD MODEL (LOCAL ONLY)
# ---------------------------
def load_model():
    global tokenizer, model

    if tokenizer is None or model is None:
        tokenizer = AutoTokenizer.from_pretrained(
            MODEL_ID,
            local_files_only=True
        )

        model = AutoModelForCausalLM.from_pretrained(
            MODEL_ID,
            local_files_only=True
        )

        model.eval()

        # FORCE CPU (avoid CUDA crash)
        model.to("cpu")

        print("✅ Model loaded successfully.")

    return tokenizer, model


# ---------------------------
# SYSTEM PROMPT
# ---------------------------
SYSTEM_PROMPT = """
You are FinSight SLM.

Provide:
- One-line interpretation per ratio.
- Then a concise 2-3 line summary.
- No calculations.
- No tables.
- Professional tone.
"""


# ---------------------------
# BUILD PROMPT
# ---------------------------
def build_prompt(category_name, ratios_dict):

    ratios_text = ""
    for key, value in ratios_dict.items():
        ratios_text += f"{key}: {value}\n"

    user_prompt = f"""
Category: {category_name}

{ratios_text}
"""

    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]


# ---------------------------
# GENERATE + FORCE STRUCTURE
# ---------------------------
def generate_response(messages, ratios_dict):

    tokenizer, model = load_model()

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.2,
            do_sample=False
        )

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)

    # Remove prompt echo
    raw_output = decoded.split("assistant")[-1].strip()

    # -----------------------------------
    # FORCE STRUCTURE (VERY IMPORTANT)
    # -----------------------------------
    sentences = raw_output.split(". ")

    structured_lines = []
    summary_lines = []

    ratio_keys = list(ratios_dict.keys())

    # Assign first N sentences to ratios
    for i, ratio in enumerate(ratio_keys):
        if i < len(sentences):
            line = sentences[i].strip()
            structured_lines.append(f"{ratio}: {line}.")
        else:
            structured_lines.append(f"{ratio}: Interpretation unavailable.")

    # Remaining sentences → summary
    remaining = sentences[len(ratio_keys):]
    if remaining:
        summary = ". ".join(remaining).strip()
        summary_lines.append(summary)

    final_output = "\n".join(structured_lines)

    if summary_lines:
        final_output += "\n\nSummary:\n" + "\n".join(summary_lines)

    return final_output
