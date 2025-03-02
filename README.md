# AI-Powered-Travel-Planner

## Overview:
The AI Powered Travel Planner helps users find the best travel options between two cities using Google Gemini AI. It provides multiple travel choices (flights, trains, buses, and cabs) with estimated costs, durations, and travel tips.

## Key Features:
1. User Inputs: Departure city, destination city, travel date, preferred mode of transport, and currency.
2. AI-Powered Recommendations: Uses Gemini AI to generate travel suggestions based on user preferences.
3. Multi-Language Support: Translates results into English, Spanish, French, German, or Hindi.
4. Sorting Options: Users can sort travel options by price or duration.
5. Clean & Minimal UI: Built using Streamlit, ensuring a user-friendly experience.

## Tech Stack:
1. Frontend: Streamlit
2. Backend: Python
3. AI Models: Google Gemini API
4. Deployment: Streamlit Cloud

## Steps:
1. Load the Google Gemini API key securely from a text file (genai_api_key.txt).
2. Set up the Streamlit UI with a centered layout and a title.
3. Create user input fields for source city, destination city, travel date, currency, preferred travel mode, sorting preference, and language selection.
4. Define AI model interaction by creating a system prompt and a user prompt with travel details.
5. Invoke Google Gemini AI to generate travel options based on user input.
6. Implement a translation feature using Googletrans to convert responses into the selected language.
7. Display AI-generated travel options, including estimated costs, durations, and important details.
8. Deploy and run the application using streamlit run app.py or a cloud service like Streamlit Cloud.

## Credits & Acknowledgment:
This project was developed as part of my internship at Innomatics Research Labs, under the guidance of Kanav Bansal Sir. I am grateful for the mentorship and learning experience provided during this internship.

## License:
This project is open-source and available under the MIT License.
