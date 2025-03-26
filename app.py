from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load intents.json
try:
    with open("intents.json", "r", encoding="utf-8") as file:
        intents = json.load(file)
except Exception as e:
    print(f"Error loading intents.json: {e}")
    intents = {"intents": []}  # Fallback to avoid crashes

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    try:
        user_message = request.json.get("message", "").strip()
        if not user_message:
            return jsonify({"response": "Please enter a valid message."})

        response = get_bot_response(user_message)
        return jsonify({"response": response})

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"response": "Sorry, something went wrong. Please try again."})

def get_bot_response(user_input):
    """
    Matches the user input with predefined intents and returns a response.
    """
    user_input = user_input.lower()

    for intent in intents.get("intents", []):
        if any(pattern.lower() in user_input for pattern in intent["patterns"]):
            return intent["responses"][0]  # Return the first matching response

    return "I'm sorry, I didn't understand that. Can you rephrase?"

if __name__ == "__main__":
    app.run(debug=True)
