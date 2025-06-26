
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create chatbot instance
chatbot = ChatBot('MyBot')
trainer = ChatterBotCorpusTrainer(chatbot)

# Train chatbot on the English corpus
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_text = request.args.get("msg")
    return str(chatbot.get_response(user_text))

if __name__ == "__main__":
    app.run(debug=True)


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize chatbot with an explicit storage adapter
chatbot = ChatBot(
    'MyBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'  # Ensures the database is properly initialized
)

# Create a new trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot
trainer.train("chatterbot.corpus.english")

# Test response
response = chatbot.get_response("Hello")
print("Bot:", response)
