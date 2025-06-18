import streamlit as st
from src.agentic_chatbot.ui.stramlit.loadui import LoadStreamlitUI

# Main Function starts
def load_agentic_chatbot_app():
    """
    Loads and runs the Langgraph AgenticAI application with Streamlit UI.
    This funciton initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for roubustness.
    
    """

    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    user_message = st.chat_input("Enter your message: ")