# main.py
from flask import Flask, request, jsonify, render_template
import openai
from autogen import Agent

app = Flask(__name__)

# Set your OpenAI API key
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the AI Agent using Autogen
agent = Agent(model="gpt-4", openai_api_key=openai.api_key)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input provided."}), 400

    try:
        response = agent.run(user_input)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
