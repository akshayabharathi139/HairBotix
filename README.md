# HairBotix
Hair Care Chatbot - AI-Powered Web Application 💇‍♀️💬
This is a Flask-based AI chatbot designed to provide personalized hair care recommendations. Users can ask about hair care routines, product suggestions, and solutions for common hair problems. The chatbot responds with detailed and structured answers based on an extensive intents.json file.

🚀 Features
✅ Interactive Web UI - A modern chat interface with smooth design and animations
✅ Hair Care Guidance - Provides expert advice on hair types, treatments, and products
✅ AI-Powered Responses - Uses an intent-based NLP approach to match user queries
✅ Easy to Customize - Update the intents.json file to add more responses
✅ Flask Backend - Handles API requests and responses efficiently

🛠 Tech Stack
🔹 Frontend: HTML, CSS, JavaScript
🔹 Backend: Flask (Python)
🔹 Database: JSON-based intent storage (intents.json)

📂 Project Structure

hairchatbot/
│── app.py    # Flask backend
│── intents.json         # AI chatbot intents & responses
│── templates/
│   └── index.html # Chatbot UI
    |__style.css
│── venv/                # Virtual environment (optional)
│── requirements.txt     # Dependencies
│── README.md            # Project documentation

 How to Run

 
1️⃣ Clone the Repository
git clone https://github.com/yourusername/hair-care-chatbot.git
cd hair-care-chatbot


2️⃣ Create & Activate Virtual Environment
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate


3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Run the Flask App
python app.py


Now visit http://127.0.0.1:5000/ in your browser! 🎨💬

📝 Customization
Modify intents.json to add more hair care tips and responses

Update index.html and styles.css to improve the UI






