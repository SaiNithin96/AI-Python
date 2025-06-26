from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined chatbot responses
responses = {
    "hello": "Hi! How can I assist you today?",
    "order status": "Please provide your order number to check the status.",
    "refund": "For refunds, please provide your order number and reason for the request.",
    "contact agent": "Connecting you to a human agent... Please wait."
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    response = responses.get(user_message, "I'm sorry, I don't understand. Can you please clarify?")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

