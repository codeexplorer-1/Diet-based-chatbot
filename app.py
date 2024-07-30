from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load responses from an external JSON file
with open('responses.json') as f:
    responses = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    bot_response = chatbot_response(user_message)
    return jsonify(response=bot_response)

def chatbot_response(user_message):
    return responses.get(user_message.lower(), "I'm sorry, I don't understand that. Could you ask something else?")

if __name__ == '__main__':
    app.run(debug=True)
