import ttkbootstrap as tb
from ttkbootstrap.constants import *
from .core import ChatBot


class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cybero – Cybersecurity Assistant")
        self.root.geometry("700x750")   # ✅ Bigger window
        self.root.minsize(700, 750)     # ✅ Prevent shrinking

        self.bot = ChatBot()

        # ================= HEADER =================
        header = tb.Label(
            root,
            text="Cybero Your Cyber Assistant",
            font=("Segoe UI", 20, "bold"),
            bootstyle="inverse-primary"
        )
        header.pack(fill=X, ipady=12)

        # ================= MAIN CONTAINER =================
        main_frame = tb.Frame(root)
        main_frame.pack(fill=BOTH, expand=True)

        # ================= CHAT AREA =================
        self.chat_area = tb.Text(
            main_frame,
            wrap="word",
            state="disabled",
            font=("Segoe UI", 12)
        )
        self.chat_area.pack(
            side=TOP,
            fill=BOTH,
            expand=True,
            padx=15,
            pady=(15, 5)
        )

        # ================= INPUT BAR (FORCED VISIBLE) =================
        input_frame = tb.Frame(root, height=70)
        input_frame.pack(fill=X, side=BOTTOM, padx=15, pady=15)
        input_frame.pack_propagate(False)  # 🔥 CRITICAL LINE

        self.user_input = tb.Entry(
            input_frame,
            font=("Segoe UI", 12)
        )
        self.user_input.pack(
            side=LEFT,
            fill=BOTH,
            expand=True,
            padx=(0, 10),
            ipady=6
        )
        self.user_input.bind("<Return>", self.send_message)

        send_button = tb.Button(
            input_frame,
            text="Send",
            bootstyle="success",
            width=10,
            command=self.send_message
        )
        send_button.pack(side=RIGHT)

        # Initial message
        self.display_message(
            "Cybero",
            "Hello! I’m Cybero 👋\nYour cybersecurity assistant.\nAsk me anything about security, SOC, malware, or phishing."
        )

    def display_message(self, sender, message):
        self.chat_area.configure(state="normal")
        self.chat_area.insert(END, f"{sender}: {message}\n\n")
        self.chat_area.configure(state="disabled")
        self.chat_area.see(END)

    def send_message(self, event=None):
        message = self.user_input.get().strip()
        if not message:
            return

        self.display_message("You", message)
        self.user_input.delete(0, END)

        if message.lower() in ["exit", "quit", "bye"]:
            self.display_message("Cybero", "Goodbye! 👋")
            return

        response = self.bot.reply(message)
        self.display_message("Cybero", response)


def main():
    root = tb.Window(themename="darkly")  # dark theme
    ChatbotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
