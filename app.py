import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Set up Gemini API
API_KEY = "YOUR API KEY"  # 🔥 Replace this with your actual API key
genai.configure(api_key=API_KEY)

def detect_sarcasm(text):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        prompt = f"Identify sarcasm in the text and highlight sarcastic words by wrapping them in asterisks (*word*). Here is the text:\n\n{text}"
        
        response = model.generate_content(prompt)
        sarcasm_result = response.text  # Get the API response text
        
        # Extract sarcastic words using a regex pattern
        sarcastic_words = re.findall(r'\*(.*?)\*', sarcasm_result)

        # Highlight sarcastic words in HTML
        for word in sarcastic_words:
            text = re.sub(r'\b' + re.escape(word) + r'\b', f'<span class="sarcastic">{word}</span>', text, flags=re.IGNORECASE)

        return text  # Return highlighted text
    except Exception as e:
        print("Error:", e)
        return "Error detecting sarcasm."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    try:
        user_text = request.form["text"]
        highlighted_text = detect_sarcasm(user_text)
        return jsonify({"highlighted_text": highlighted_text})
    except Exception as e:
        print("Flask Error:", e)
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
