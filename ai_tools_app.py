import streamlit as st

# Page config
st.set_page_config(page_title="AI Tools Class", layout="wide")

# Sidebar navigation
page = st.sidebar.radio("Navigation", ["Home", "About", "Tools", "Contact"])

# Home Page
if page == "Home":
    st.title("AI Tools Online Class")
    st.write("Learn the most powerful AI tools step by step and use them in your daily work, study, and business.")

# About Page
elif page == "About":
    st.header("About the Class")
    st.write("""
    This course is designed for beginners and professionals to explore modern AI tools.
    
    **Trainer**: John Doe (AI Specialist)  
    **Duration**: 6 Weeks Online  
    """)

# Tools Page
elif page == "Tools":
    st.header("AI Tools Covered")
    tools = [
        "ChatGPT - Text Generation",
        "MidJourney - AI Art",
        "Google Gemini - Search + AI",
        "Claude AI - Writing & Reasoning",
        "GitHub Copilot - Coding Assistant"
    ]
    for tool in tools:
        st.write(f"- {tool}")

# Contact Page
elif page == "Contact":
    st.header("Contact Us")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    
    if st.button("Send"):
        st.success("✅ Your message has been sent!")
