# ============================================================
# 🛡️ SAFEGUARD AI — SAFETY ENGINE
# ============================================================

import re


# ============================================================
# PROFANITY KEYWORDS
# ============================================================

PROFANITY_WORDS = {
    "english": [
        "fuck",
        "fucking",
        "shit",
        "bitch",
        "asshole",
        "idiot",
        "stupid",
        "bastard",
        "dumbass",
    ],

    "tamil": [
        "thevidiya",
        "thevidiya paiya",
        "punda",
        "pundai",
        "otha",
        "ootha",
        "baadu",
        "loosu",
        "naaye",
        "nayee",
    ],

    "hindi": [
        "madarchod",
        "bhosdi",
        "chutiya",
        "gandu",
        "kamina",
        "harami",
    ],

    "telugu": [
        "lanja",
        "dengey",
        "puka",
        "erripuka",
    ],

    "malayalam": [
        "myre",
        "poda",
        "patti",
    ],

    "kannada": [
        "bolimaga",
        "sulemaga",
        "yenne",
    ],
}


# ============================================================
# COMBINED WORD LIST
# ============================================================

ALL_BAD_WORDS = []

for words in PROFANITY_WORDS.values():
    ALL_BAD_WORDS.extend(words)

ALL_BAD_WORDS = sorted(
    set(ALL_BAD_WORDS),
    key=len,
    reverse=True
)


# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize_text(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ============================================================
# LANGUAGE DETECTION
# ============================================================

def detect_language(text):
    text = normalize_text(text)

    for language, words in PROFANITY_WORDS.items():
        for word in words:
            if re.search(
                r"(?<!\w)" + re.escape(word) + r"(?!\w)",
                text
            ):
                return language.title()

    # Basic Unicode-based detection
    if re.search(r"[\u0B80-\u0BFF]", text):
        return "Tamil"

    if re.search(r"[\u0900-\u097F]", text):
        return "Hindi"

    if re.search(r"[\u0C00-\u0C7F]", text):
        return "Telugu"

    if re.search(r"[\u0D00-\u0D7F]", text):
        return "Malayalam"

    if re.search(r"[\u0C80-\u0CFF]", text):
        return "Kannada"

    return "English"


# ============================================================
# PROFANITY DETECTION
# ============================================================

def detect_profanity(text):

    text = normalize_text(text)

    matched_words = []

    for word in ALL_BAD_WORDS:

        pattern = (
            r"(?<!\w)"
            + re.escape(word)
            + r"(?!\w)"
        )

        if re.search(pattern, text):
            matched_words.append(word)

    return bool(matched_words), matched_words


# ============================================================
# MASK CONTENT
# ============================================================

def mask_profanity(text):

    if not isinstance(text, str):
        return ""

    result = text

    for word in ALL_BAD_WORDS:

        pattern = (
            r"(?<!\w)"
            + re.escape(word)
            + r"(?!\w)"
        )

        result = re.sub(
            pattern,
            "[CONTENT REMOVED]",
            result,
            flags=re.IGNORECASE
        )

    return result


# ============================================================
# MAIN TEXT ANALYSIS
# ============================================================

def analyze_text(text):

    detected, matched_words = detect_profanity(text)

    masked_text = mask_profanity(text)

    if detected:

        return {
            "safe": False,
            "category": "Profanity / Abusive Language",
            "matched_words": matched_words,
            "masked_text": masked_text,
            "warning": "⚠️ Offensive language detected."
        }

    return {
        "safe": True,
        "category": "Safe",
        "matched_words": [],
        "masked_text": text,
        "warning": "✅ No known offensive language detected."
    }


# ============================================================
# APP COMPATIBILITY FUNCTION
# ============================================================

def analyze_message(text):

    result = analyze_text(text)

    language = detect_language(text)

    if result["safe"]:
        toxicity_label = "Low"
        risk_level = "Low"
    else:
        toxicity_label = "High"
        risk_level = "High"

    return {
        "language": language,
        "toxicity_label": toxicity_label,
        "risk_level": risk_level,
        "protected_text": result["masked_text"],
        "safe": result["safe"],
        "category": result["category"],
        "matched_words": result["matched_words"],
        "warning": result["warning"],
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print("🛡️ SAFEGUARD AI Safety Engine")
    print("=" * 45)

    tests = [
        "Hello, have a nice day!",
        "You are an idiot.",
        "This is a normal message."
    ]

    for message in tests:

        result = analyze_message(message)

        print("\nOriginal :", message)
        print("Safe     :", result["safe"])
        print("Language :", result["language"])
        print("Toxicity :", result["toxicity_label"])
        print("Risk     :", result["risk_level"])
        print("Visible  :", result["protected_text"])
