import streamlit as st
import google.generativeai as genai
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stylable_container import stylable_container
from gtts import gTTS
from fpdf import FPDF
import re
import io

# Configure Gemini API
genai.configure(api_key="AIzaSyBbcPmilYx3mvi-bWCCZMkCfFE2BOHMTnY")  

# Page setup
st.set_page_config(
    page_title=" StudyBot AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Session state for persistence
if "response_text" not in st.session_state:
    st.session_state.response_text = ""
if "user_query" not in st.session_state:
    st.session_state.user_query = ""
if "history" not in st.session_state:
    st.session_state.history = []

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("<h1 style='color: Black;'>🤖 StudyBot</h1><p style='color: #a1a1a1;'>Your AI-powered learning assistant</p>", unsafe_allow_html=True)
    st.markdown("### Features")
    with stylable_container(key="f1", css_styles="{background-color: rgba(255,255,255,0.1); border-radius: 12px; padding: 15px; margin-bottom: 15px;}"):
        st.markdown("📚 **Instant Answers**\n\nGet detailed explanations for any academic question")
    with stylable_container(key="f2", css_styles="{background-color: rgba(255,255,255,0.1); border-radius: 12px; padding: 15px; margin-bottom: 15px;}"):
        st.markdown("💡 **Learning Support**\n\nUnderstand complex concepts with simple explanations")
    st.markdown("---")
    st.markdown("### About")
    st.markdown("StudyBot uses Google's Gemini AI to provide intelligent responses to your academic questions.")

# Header
colored_header("Ask StudyBot Anything", "Get instant answers to your academic questions", color_name="blue-70")

# Input Area
col1, col2 = st.columns([3, 1])
with col1:
    with stylable_container(key="input", css_styles="{background-color: white; border-radius: 12px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);}"):
        user_query = st.text_input("Enter your question:", placeholder="e.g. Explain quantum physics in simple terms", key="query_input")
        answer_type = st.radio("Select answer type:", ["Short Summary", "Detailed Explanation"], horizontal=True)
        submit_button = st.button("Get Answer 🚀", use_container_width=True)

with col2:
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712035.png" width="150">
        <h4 style="color: #333;">Your AI Study Assistant</h4>
    </div>
    """, unsafe_allow_html=True)

# Process question
if submit_button and user_query:
    st.session_state.user_query = user_query  # Save user query
    with st.spinner("🧠 Thinking... Please wait"):
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            query = f"{user_query}. Give a {'brief summary' if answer_type == 'Short Summary' else 'detailed explanation'}."
            response = model.generate_content(query)

            if response and hasattr(response, 'text'):
                text = response.text.strip()
                st.session_state.response_text = text  # Save to session_state
                st.session_state.history.append((user_query, text))
            else:
                st.warning("No response content found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Display question & answer
if st.session_state.response_text:
    st.markdown(f"""
    <div style="background-color: rgba(102, 126, 234, 0.1); border-radius: 12px; padding: 15px; margin: 15px 0;">
        <p style="margin: 0; font-weight: 600;">You asked:</p>
        <p style="margin: 0;">{st.session_state.user_query}</p>
    </div>
    """, unsafe_allow_html=True)

    first_sentence, *rest = re.split(r'(?<=[.!?])\s+', st.session_state.response_text.strip(), maxsplit=1)
    formatted = f"**{first_sentence}**"
    if rest:
        formatted += " " + rest[0]
    st.subheader("🤖 AI Response")
    st.markdown(formatted)

    # 🔊 Text-to-Speech
    if st.button("🔊 Listen to Answer"):
        try:
            tts = gTTS(st.session_state.response_text)
            audio_bytes = io.BytesIO()
            tts.write_to_fp(audio_bytes)
            audio_bytes.seek(0) 
            st.audio(audio_bytes, format="audio/mp3")
        except Exception as e:
            st.error(f"Text-to-speech failed: {e}")

    # 📄 Download PDF
    if st.button("📄 Download as PDF"):
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)
            for line in st.session_state.response_text.split('\n'):
                pdf.multi_cell(0, 10, line)
            pdf_bytes = pdf.output(dest='S').encode('latin1')  # Corrected line
            st.download_button("Download PDF", data=pdf_bytes, file_name="studybot_answer.pdf", mime="application/pdf")
        except Exception as e:
            st.error(f"PDF generation failed: {e}")


# History
if st.session_state.history:
    with st.expander("📚 Recent Questions & Answers"):
        for q, a in st.session_state.history[-5:]:
            st.markdown(f"**Q:** {q}")
            st.markdown(f"**A:** {a}")
            st.markdown("---")
