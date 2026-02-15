from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# ==========================================
# CONFIG
# ==========================================

MODEL_ID = "Mihirsingh1101/smolified-finsight-ratio-interpreter"

_tokenizer = None
_model = None
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# ==========================================
# LOAD MODEL (SAFE + STABLE)
# ==========================================

def load_model():
    global _tokenizer, _model

    if _tokenizer is None or _model is None:
        print("🔹 Loading FinSight SLM...")

        _tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

        # 🔥 IMPORTANT: No FP16, No device_map auto
        _model = AutoModelForCausalLM.from_pretrained(MODEL_ID)

        _model.to(_device)
        _model.eval()

        print("✅ Model loaded successfully.")

    return _tokenizer, _model


# ==========================================
# SYSTEM PROMPT
# ==========================================

SYSTEM_PROMPT = """
You are FinSight SLM, a professional financial diagnostic AI.

The user provides financial ratios for a category.

You must:
• Provide one-line interpretation per ratio.
• Provide a concise 2–3 line category summary.
• Adapt tone based on severity.
• Avoid repetition.
• Do NOT calculate.
• Do NOT generate tables.
• Keep output structured and professional.
"""


# ==========================================
# BUILD PROMPT
# ==========================================

def build_prompt(category_name, ratios_dict):

    ratios_text = ""
    for key, value in ratios_dict.items():
        ratios_text += f"{key}: {value}\n"

    user_prompt = f"""
Category: {category_name}

{ratios_text}
"""

    return [
        {"role": "system", "content": SYSTEM_PROMPT.strip()},
        {"role": "user", "content": user_prompt.strip()}
    ]


# ==========================================
# GENERATE RESPONSE (CUDA SAFE)
# ==========================================

def generate_response(messages):

    tokenizer, model = load_model()

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    if text.startswith("<bos>"):
        text = text.replace("<bos>", "")

    inputs = tokenizer(
        text,
        return_tensors="pt"
    ).to(_device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=300,
            do_sample=False,     # 🔥 NO SAMPLING (CUDA SAFE)
        )

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)

    # Remove prompt from output safely
    cleaned_output = decoded.replace(text, "").strip()

    return cleaned_output
