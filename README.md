# AI-Powered Chatbot

## Overview
This AI-Powered Chatbot project is designed to provide users with intelligent, real-time responses to queries. It features natural language processing (NLP) capabilities, conversation history storage, and integrations with external APIs for weather, news, and more.

---

## Key Features
1. **Natural Language Processing (NLP):**
   - Uses SpaCy for processing user input.
   - Pre-trained TensorFlow/Keras models for generating intelligent responses.

2. **Conversation History:**
   - Stores user-bot interactions in an SQLite database.
   - Easily retrievable for future reference or analysis.

3. **External API Integration:**
   - Examples include weather and news retrieval using external APIs.

4. **Lightweight and Scalable:**
   - Built on Flask, making it easy to deploy and scale.

---

## Technologies Used
- **Programming Language:** Python
- **Framework:** Flask
- **Database:** SQLite
- **NLP Libraries:** SpaCy, TensorFlow/Keras
- **APIs:** Placeholder for weather and news APIs

---

## Setup Instructions
### Prerequisites
- Python 3.8+
- Pip (Python package manager)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/stephenombuya/-AI-Powered-Chatbot
   cd ai-powered-chatbot
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the SQLite database:
   ```bash
   python
   >>> from app import init_db
   >>> init_db()
   >>> exit()
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Access the chatbot at `http://127.0.0.1:5000`.

---

## API Endpoints
1. **Chat Endpoint**
   - URL: `/chat`
   - Method: `POST`
   - Payload Example:
     ```json
     {
       "message": "Hello, chatbot!"
     }
     ```
   - Response Example:
     ```json
     {
       "response": "I'm here to help!"
     }
     ```

2. **History Endpoint**
   - URL: `/history`
   - Method: `GET`
   - Response Example:
     ```json
     [
       {
         "user_message": "Hello",
         "bot_response": "Hi there!",
         "timestamp": "2025-01-08 12:30:45"
       }
     ]
     ```

3. **External API Endpoint**
   - URL: `/api`
   - Method: `GET`
   - Query Parameters:
     - `type`: `weather` or `news`
   - Response Example:
     ```json
     {
       "weather": "Sunny, 25°C"
     }
     ```

---

## File Structure
- `app.py`: Main application logic
- `chat_history.db`: SQLite database for storing conversation history
- `requirements.txt`: Dependencies for the project
- `README.md`: Project documentation
- `chatbot_model.h5`: Pre-trained model (assumed to be in the root directory)

---

## Future Improvements
1. Enhance NLP capabilities with advanced models (e.g., GPT, BERT).
2. Add more external API integrations (e.g., stock market, sports updates).
3. Implement a frontend interface for better user interaction.
4. Improve database management and add analytics.

---

## Contribution Guidelines
1. Fork the repository and create your branch:
   ```bash
   git checkout -b feature-name
   ```
2. Commit your changes and push them:
   ```bash
   git commit -m "Add feature-name"
   git push origin feature-name
   ```
3. Submit a pull request for review.

---

## License
This project is licensed under the Apache 2.0 License. See the `LICENSE` file for details.

---

## Contact
For questions or support, contact [Stephen Ombuya](https://github.com/stephenombuya).

