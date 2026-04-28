from flask import Flask, request, jsonify
from agents.orchestrator import orchestrate

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = orchestrate(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
