from flask import Flask, request, jsonify
import sqlite3
import random
import spacy
import tensorflow as tf
from tensorflow.keras.models import load_model
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Load NLP model and data
nlp = spacy.load("en_core_web_sm")
model = load_model("chatbot_model.h5")  # Assuming you have a pre-trained model

# Database setup
def init_db():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS chat_history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_message TEXT,
                        bot_response TEXT,
                        timestamp TEXT)''')
    conn.commit()
    conn.close()

# Save conversation history
def save_to_db(user_message, bot_response):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_history (user_message, bot_response, timestamp) VALUES (?, ?, ?)",
                   (user_message, bot_response, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()

# Dummy responses (to be replaced with NLP logic or pre-trained model outputs)
def generate_response(user_input):
    # Example: basic hardcoded responses
    responses = [
        "I'm here to help!",
        "Can you clarify your question?",
        "That's interesting. Tell me more.",
    ]
    return random.choice(responses)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "Message content is missing."}), 400

    # Process input and generate response
    response = generate_response(user_message)

    # Save the conversation history
    save_to_db(user_message, response)

    return jsonify({"response": response})

@app.route('/history', methods=['GET'])
def history():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_message, bot_response, timestamp FROM chat_history ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    history = [
        {"user_message": row[0], "bot_response": row[1], "timestamp": row[2]} for row in rows
    ]
    return jsonify(history)

@app.route('/api', methods=['GET'])
def external_api():
    # Example: API integration (dummy example for weather and news)
    query_type = request.args.get('type')
    if query_type == 'weather':
        # Integrate a weather API like OpenWeatherMap
        return jsonify({"weather": "Sunny, 25°C"})
    elif query_type == 'news':
        # Integrate a news API like NewsAPI
        return jsonify({"news": "Breaking News: AI Chatbots are taking over!"})
    else:
        return jsonify({"error": "Invalid query type."}), 400

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
