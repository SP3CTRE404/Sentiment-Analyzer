import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title = "Sentiment Analyser",
    layout = "centered"
)

try :
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Google_API_KEY not found. please set it in your .env file.")
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"Error Configuring API: {e}")
    st.stop()

def get_sentiment(text):
    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = f"""
    As an expert sentiment analysis AI, classify the sentiment of the following text.
    The sentiment can only be one of three options: Positive, Negative, or Neutral.
    Return only a single word.

    Text: "{text}"
    Sentiment:
    """

    try:
        response = model.generate_content(prompt)
        sentiment = response.text.strip()
        return sentiment
    except Exception as e:
        return f"Error: Could not analyze sentiment. {e}"
    
st.title("Sentiment Analyser")
st.markdown("Enter text to analyze its sentiment.")

user_text = st.text_area("Your Tet Here:", height = 150, placeholder = "Example: The movie was a masterpiece, truly captivating from start to finish!")

if st.button("Analyze Sentiment"):
    if user_text:
        with st.spinner("Analyzing..."):
            sentiment = get_sentiment(user_text)

            st.subheader("Analysis Result")

            if "Positive" in sentiment:
                st.success(f"**Positive**")
            elif "Positive" in sentiment:
                st.error(f"**Negative**")
            elif "Positive" in sentiment:
                st.info(f"**Neutral**")
            else:
                st.warning(sentiment)
else:
    st.info("Please enter text and click 'Analyze Sentiment' to see the result.")
    