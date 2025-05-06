from flask import Flask, render_template, request
from bot import ChurnBot

app = Flask(__name__)
bot = ChurnBot(api_key="AIzaSyB5OOuWTpGJufz6Zh0lTdn67_Cx1m7CXBM")

# Store conversation history in a list
chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        try:
            reply = bot.chat.send_message(
                f"You are a churn analysis assistant. {user_input}, make response 1 line"
            )
            response = reply.text
            chat_history.append(("You", user_input))
            chat_history.append(("ChurnBot", response))
        except Exception as e:
            response = f"❌ Error: {e}"
            chat_history.append(("Error", str(e)))

    return render_template("chat.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
