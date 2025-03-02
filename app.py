import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from googletrans import Translator
import os

def load_api_key(filepath):
    try:
        with open(filepath, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        raise Exception(f"❌ API key file '{filepath}' not found!")

GOOGLE_API_KEY = load_api_key("genai_api_key.txt")

st.set_page_config(page_title="AI Travel Assistant", layout="centered")

st.markdown("<h1 style='text-align: center;'>AI Powered Travel Planner</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    source_city = st.text_input("🛫 Departure City", placeholder="E.g., New Delhi")
    destination_city = st.text_input("📍 Destination City", placeholder="E.g., Amsterdam")
    travel_date = st.date_input("📅 Travel Date")
    currency = st.selectbox("💲 Select Currency", ["USD", "INR", "EUR", "GBP", "JPY"])

with col2:
    preferred_mode = st.selectbox("🚗 Preferred Mode", ["Any", "Flight", "Train", "Bus", "Cab"])
    sort_by = st.radio("📊 Sort By", ["Price", "Duration"])
    language = st.selectbox("🌍 Select Language", ["English", "Spanish", "French", "German", "Hindi"])

language_codes = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
}

def get_travel_options(source, destination, mode, currency):
    system_prompt = SystemMessage(
        content="You are an AI-powered travel assistant. Provide multiple travel options (cab, train, bus, flight) with estimated costs, duration, and relevant travel tips."
    )
    user_prompt = HumanMessage(
        content=f"I am traveling from {source} to {destination} in {currency}. Preferred mode: {mode}. Suggest travel options with estimated cost, duration, and important details."
    )

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", google_api_key=GOOGLE_API_KEY)

    try:
        response = llm.invoke([system_prompt, user_prompt])
        return response.content if response else "⚠ No response from AI."
    except Exception as e:
        return f"❌ Error fetching travel options: {str(e)}"

def translate_text(text, target_language):
    if target_language == "English":
        return text
    translator = Translator()
    return translator.translate(text, dest=language_codes.get(target_language, "en")).text

if st.button("🔍 Find Travel Options"):
    if source_city.strip() and destination_city.strip():
        with st.spinner("🔄 Fetching best travel options..."):
            travel_info = get_travel_options(source_city, destination_city, preferred_mode, currency)
        st.success("✅ AI-Generated Travel Recommendations:")
        st.markdown(travel_info)
    else:
        st.warning("⚠ Please enter both source and destination locations.")

st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            background-color: #f1f1f1;
            color: #333333;
            font-weight: bold;
            border-top: 2px solid #cccccc;
            z-index: 9999;
        }
    </style>
    <div class="footer">
        Created by Paul Andrew 🚀
    </div>
    """,
    unsafe_allow_html=True
)
