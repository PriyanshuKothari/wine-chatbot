from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Ensure you have set the OPENAI_API_KEY in your Heroku config
openai.api_key = os.getenv("sk-None-BGPsJcmSNBXkIdNzM1YHT3BlbkFJghlLJjAQbvOaMWXlICPt")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
