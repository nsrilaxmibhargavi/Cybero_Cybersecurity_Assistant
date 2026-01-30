import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import scrolledtext
from chatbot.core import ChatBot

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cybersecurity Chatbot")
        self.root.geometry("520x620")
        self.root.resizable(False, False)

        self.bot = ChatBot()

        # Header
        header = tb.Label(
            root,
            text="Cybersecurity Chatbot",
            font=("Segoe UI", 16, "bold")
        )
        header.pack(pady=10)

        # Chat area
        self.chat_area = scrolledtext.ScrolledText(
            root,
            wrap="word",
            font=("Segoe UI", 11),
            state="disabled",
            height=25
        )
        self.chat_area.pack(padx=15, pady=10, fill="both", expand=True)

        # Input frame
        input_frame = tb.Frame(root)
        input_frame.pack(padx=15, pady=15, fill="x")

        self.user_input = tb.Entry(
            input_frame,
            font=("Segoe UI", 11)
        )
        self.user_input.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", self.send_message)

        send_button = tb.Button(
            input_frame,
            text="Send",
            bootstyle="success",
            command=self.send_message
        )
        send_button.pack(side="right")

        self.display_message("Bot", "Hello! I’m your cybersecurity assistant. Ask me anything.")

    def display_message(self, sender, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert("end", f"{sender}: {message}\n\n")
        self.chat_area.config(state="disabled")
        self.chat_area.yview("end")

    def send_message(self, event=None):
        message = self.user_input.get().strip()
        if not message:
            return

        self.display_message("You", message)
        self.user_input.delete(0, "end")

        if message.lower() in ["exit", "quit", "bye"]:
            self.display_message("Bot", "Goodbye! 👋")
            return

        response = self.bot.reply(message)
        self.display_message("Bot", response)

def run_gui():
    root = tb.Window(themename="flatly")  # try: darkly, cyborg, superhero
    app = ChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
