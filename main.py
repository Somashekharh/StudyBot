import streamlit as st
import google.generativeai as genai
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stylable_container import stylable_container

# Initialize the Google Gemini client
genai.configure(api_key="AIzaSyBbcPmilYx3mvi-bWCCZMkCfFE2BOHMTnY")  # Replace with your actual API key

# Set up the Streamlit app with custom theme
st.set_page_config(
    page_title="🤖 StudyBot AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    .stTextInput>div>div>input {
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        padding: 12px;
    }

    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 24px;
        font-weight: 600;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

    .ai-response {
        background-color: white;
        border-radius: 16px;
        padding: 24px;
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border-left: 4px solid #667eea;
    }

    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2c3e50 0%, #1a1a2e 100%);
        color: black;
    }

    .logo-container {
        text-align: center;
        margin-bottom: 30px;
    }

    .feature-card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar with app info and features
with st.sidebar:
    st.markdown("""
    <div class="logo-container">
        <h1 style="color: white;">🤖 StudyBot</h1>
        <p style="color: #a1a1a1;">Your AI-powered learning assistant</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Features")
    with stylable_container(
            key="feature1",
            css_styles="""
            {
                background-color: rgba(255,255,255,0.1);
                border-radius: 12px;
                padding: 15px;
                margin-bottom: 15px;
            }
            """
    ):
        st.markdown("📚 **Instant Answers**\n\nGet detailed explanations for any academic question")

    with stylable_container(
            key="feature2",
            css_styles="""
            {
                background-color: rgba(255,255,255,0.1);
                border-radius: 12px;
                padding: 15px;
                margin-bottom: 15px;
            }
            """
    ):
        st.markdown("💡 **Learning Support**\n\nUnderstand complex concepts with simple explanations")

    st.markdown("---")
    st.markdown("### About")
    st.markdown("StudyBot uses Google's Gemini AI to provide intelligent responses to your academic questions.")

# Main content area
colored_header(
    label="Ask StudyBot Anything",
    description="Get instant answers to your academic questions",
    color_name="blue-70",
)

# Layout using columns
col1, col2 = st.columns([3, 1])

with col1:
    with stylable_container(
            key="input_container",
            css_styles="""
            {
                background-color: white;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            """
    ):
        user_query = st.text_input(
            "Enter your question:",
            placeholder="e.g. Explain quantum physics in simple terms",
            key="user_input"
        )

        # Add a submit button with icon
        submit_button = st.button("Get Answer 🚀", use_container_width=True)

with col2:
    # Placeholder for logo or illustration
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712035.png" width="150">
        <h4 style="color: #333;">Your AI Study Assistant</h4>
    </div>
    """, unsafe_allow_html=True)

# If the user submits a query
if submit_button and user_query:
    st.markdown(f"""
    <div style="background-color: rgba(102, 126, 234, 0.1);
                border-radius: 12px;
                padding: 15px;
                margin: 15px 0;">
        <p style="margin: 0; font-weight: 600;">You asked:</p>
        <p style="margin: 0;">{user_query}</p>
    </div>
    """, unsafe_allow_html=True)

    # Add a loading spinner
    with st.spinner("🧠 Thinking... Please wait"):
        try:
            # Create a model instance
            model = genai.GenerativeModel("gemini-1.5-flash")  # or gemini-pro

            # Generate content from the model
            response = model.generate_content(user_query)

            # Display the response in a styled container
            if response and hasattr(response, 'text'):
                with stylable_container(
                        key="response_container",
                        css_styles="""
                        {
                            background-color: white;
                            border-radius: 16px;
                            padding: 24px;
                            margin-top: 20px;
                            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                            border-left: 4px solid #667eea;
                        }
                        """
                ):
                    st.subheader("🤖 AI Response")
                    st.markdown(response.text)
            else:
                st.warning("No response content found.")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Add some empty space at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)