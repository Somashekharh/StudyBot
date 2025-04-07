
# 🤖 StudyBot AI

StudyBot AI is an interactive, AI-powered study assistant built with [Streamlit](https://streamlit.io/) and powered by Google's **Gemini AI** (via `google.generativeai`). It provides quick, intelligent answers to academic questions and helps users understand complex concepts in a simple and engaging way.

![StudyBot Preview](https://cdn-icons-png.flaticon.com/512/4712/4712035.png)

---

## ✨ Features

- 📚 **Instant Answers** – Ask any academic question and get instant, detailed responses.
- 💡 **Learning Support** – Simplifies complex concepts to boost your understanding.
- 🎨 **Custom UI/UX** – Aesthetic, user-friendly interface with modern design.
- ⚡ **Responsive Layout** – Works well on desktops and tablets.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/studybot-ai.git
cd studybot-ai
```

### 2. Install Requirements

Make sure you have Python 3.7+ and `pip` installed.

```bash
pip install -r requirements.txt
```

### 3. Add Your API Key

Replace the placeholder API key in the script with your actual **Google Gemini API Key**:

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

---

## 🧠 Usage

Start the Streamlit app:

```bash
streamlit run app.py
```

Once launched, open the provided local URL in your browser (e.g., `http://localhost:8501`).

---

## 🛠️ Dependencies

- `streamlit`
- `google-generativeai`
- `streamlit-extras`

You can install them manually:

```bash
pip install streamlit google-generativeai streamlit-extras
```

Or use a `requirements.txt` file like this:

```
streamlit
google-generativeai
streamlit-extras
```

---

## 📁 File Structure

```
studybot-ai/
│
├── app.py              # Main Streamlit application
├── README.md           # Project overview (this file)
├── requirements.txt    # Python dependencies
```

---

## 🔐 Security Note

Do **not** expose your API key in public repositories. Use environment variables or secrets management if deploying online.

---
