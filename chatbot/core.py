from .nlp import match_intent, is_follow_up
from .responses import RESPONSES
from datetime import datetime
import os
import random

class ChatBot:
    def __init__(self):
        self.last_intent = None  # 🧠 context memory

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logs_dir = os.path.join(base_dir, "logs")

        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        self.log_file = os.path.join(logs_dir, "chats.log")

    def log_chat(self, user_input, bot_response):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] USER: {user_input}\n")
            f.write(f"[{timestamp}] BOT: {bot_response}\n")

from .nlp import match_intent, is_follow_up
from .responses import RESPONSES
from .ai_fallback import ai_reply
from datetime import datetime
import os
import random

class ChatBot:
    def __init__(self):
        self.last_intent = None

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logs_dir = os.path.join(base_dir, "logs")
        os.makedirs(logs_dir, exist_ok=True)

        self.log_file = os.path.join(logs_dir, "chats.log")

    def log_chat(self, user_input, bot_response):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] USER: {user_input}\n")
            f.write(f"[{timestamp}] CYBERO: {bot_response}\n")

    def reply(self, user_input):
        # 1️⃣ Follow-up handling
        if is_follow_up(user_input) and self.last_intent:
            intent = self.last_intent
        else:
            intent = match_intent(user_input)
    
        # 2️⃣ Known intent → rule-based response
        if intent != "fallback" and intent in RESPONSES:
            response = random.choice(RESPONSES[intent])
            self.last_intent = intent
    
        # 3️⃣ Fallback intent → AI response
        else:
            try:
                response = ai_reply(
                    user_input,
                    context=self.last_intent
                )
            except Exception:
                response = random.choice(RESPONSES["fallback"])
    
        self.log_chat(user_input, response)
        return response
    

