# AI-Powered Sentiment Analyzer

A simple yet powerful web application that analyzes the sentiment of any given text and classifies it as Positive, Negative, or Neutral. This tool leverages the advanced reasoning capabilities of Google's Gemini family of models to provide real-time, accurate sentiment analysis.
### Key Features

    Intelligent Analysis: Utilizes a powerful Large Language Model (LLM) via the Google Gemini API for nuanced and context-aware sentiment classification.

    Simple Web Interface: Built with Streamlit for a clean, fast, and user-friendly experience. No complex setup required.

    Real-Time Feedback: Get instant sentiment analysis with a clear, color-coded result.

    Multilingual Capabilities: Thanks to the underlying power of the Gemini model, this tool can analyze sentiment in a wide variety of languages, not just English. Simply input text in another language to test it!

### How It Works

The application follows a straightforward process:

    User Input: The user enters a piece of text into the web interface.

    Prompt Engineering: The application takes the input text and embeds it within a carefully crafted prompt. This prompt instructs the AI to act as a sentiment analysis expert and classify the text.

    API Integration: The prompt is sent to the Google Gemini API, which processes the request using its advanced language understanding.

    Display Result: The API returns a single-word classification (Positive, Negative, or Neutral), which is then displayed to the user with a corresponding emoji and color.

### Getting Started

Follow these instructions to set up and run the project on your local machine.
Prerequisites

    Python 3.8 or higher

    Git

1. Clone the Repository

First, clone this repository to your local machine.

git clone <your-repository-url>
cd gemini-sentiment-app

2. Install Dependencies

Install the required Python packages using pip.

pip install -r requirements.txt

(Note: If you don't have a requirements.txt file yet, you can create one with pip freeze > requirements.txt after installing the packages manually: pip install streamlit google-generativeai python-dotenv)
3. Set Up Your API Key

    Create a file named .env in the root of your project folder.

    Get your API key from Google AI Studio.

    Add your API key to the .env file like this:

    GOOGLE_API_KEY="YOUR_API_KEY_HERE"

4. Run the Application

Start the Streamlit server with the following command:

streamlit run app.py

Your web browser should automatically open with the application running.
### Future Enhancements

    Sentiment Score: Display a confidence score (e.g., 95% Positive) alongside the classification.

    Text Summarization: Add a feature to summarize the input text.

    Aspect-Based Sentiment: Analyze sentiment towards specific features or topics within the text (e.g., "The food was great, but the service was slow.").

Feel free to contribute to this project by forking it and creating a pull request.