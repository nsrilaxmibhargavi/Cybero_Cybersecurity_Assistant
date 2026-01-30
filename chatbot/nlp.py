import re
from .intents import INTENTS

FOLLOW_UP_PHRASES = [
    "tell me more",
    "more",
    "explain more",
    "continue",
    "details",
    "go on"
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.strip()

def is_follow_up(user_input):
    user_input = clean_text(user_input)
    return user_input in FOLLOW_UP_PHRASES

def match_intent(user_input):
    user_input = clean_text(user_input)

    for intent, data in INTENTS.items():
        for keyword in data["keywords"]:
            if keyword in user_input:
                return intent

    return "fallback"
