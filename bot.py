import google.generativeai as genai

class ChurnBot:
    def __init__(self, api_key):
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.chat = self.model.start_chat(history=[])  # enable chat history
        print("🤖 ChurnBot initialized. Ask anything about customer churn.\n(Type 'exit' to quit.)\n")

    def chat_loop(self):
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("ChurnBot: 👋 Goodbye!")
                break

            try:
                response = self.chat.send_message(
                    f"You are a churn analysis assistant. {user_input}, make response 1 line"
                )
                print(f"ChurnBot: {response.text}\n")
            except Exception as e:
                print(f"❌ Error: {e}")

    def print_history(self):
        print("\n🕘 Chat History:")
        for idx, message in enumerate(self.chat.history, 1):
            print(f"{idx}. {message.role.capitalize()}: {message.parts[0].text}")

# ---- Run bot ----
if __name__ == "__main__":
    API_KEY = "AIzaSyB5OOuWTpGJufz6Zh0lTdn67_Cx1m7CXBM"  
    bot = ChurnBot(api_key=API_KEY)
    bot.chat_loop()
    bot.print_history()
