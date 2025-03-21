# 🤖 Sarcasm Detector

A simple web-based sarcasm detection system that uses Google's **Gemini AI** to analyze text and highlight sarcastic words.

## 🚀 Features
- Detects sarcasm in user-inputted text
- Highlights sarcastic words in the output
- User-friendly interface with a background image
- Flask backend with JavaScript-based frontend

## 📂 Project Structure
```
📁 sarcasm_detector
│-- 📁 static
│   │-- 📄 style.css  (Styling for the app)
│   │-- 📄 script.js  (Handles frontend interactions)
│   │-- 📁 assets
│   │   │-- 🖼 bg.jpg  (Background image)
│-- 📁 templates
│   │-- 📄 index.html  (Main webpage UI)
│-- 📄 app.py  (Flask backend)
│-- 📄 requirements.txt  (Dependencies)
│-- 📄 README.md  (This file)
```

##  Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/dhina547/sarcasm_detector.git
cd sarcasm_detector
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate (Mac/Linux)
venv\Scripts\activate  # Activate (Windows)
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Add Your Google API Key in `app.py`**
Replace `YOUR_API_KEY_HERE` with your actual Google API key:
```python
API_KEY = "YOUR_API_KEY_HERE"
genai.configure(api_key=API_KEY)
```

### **5️⃣ Run the Flask App**
```sh
python app.py
```
The app will run on `http://127.0.0.1:5000/`

##  How to Use
1️⃣ Open the web app in your browser.
2️⃣ Enter a sarcastic sentence in the text box.
3️⃣ Click the **Analyze** button.
4️⃣ The system will detect sarcasm and highlight the sarcastic words.

## 🛠 Technologies Used
- **Flask** (Backend)
- **HTML, CSS, JavaScript** (Frontend)
- **Google Gemini AI** (Sarcasm Detection)

##   License
This project is open-source and available under the **MIT License**.

## 🤝 Contributing
Contributions are welcome! Feel free to submit pull requests or report issues.

## 🌎 Connect
- **GitHub:** [github.com/dhina547](https://github.com/dhina547)
- **Email:** dhinagar547@gmail.com


---
🚀 **Happy Coding!**

