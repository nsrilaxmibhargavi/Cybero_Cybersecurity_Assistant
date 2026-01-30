from chatbot.core import ChatBot

def main():
    bot = ChatBot()
    print("Chatbot is running. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break

        response = bot.reply(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
