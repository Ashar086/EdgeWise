import streamlit as st
import pandas as pd
import random

# Introduction and Disclaimer
st.title("Edge Device Content Moderation Bot")
st.write("""
This application is designed for content moderation and works best with local deployment.
For more details, visit https://github.com/vikashkodati/nextedge-morpheus/tree/main.
Please note that this is just a cloud deployment as a part of the submission.
""")

# Load the CSV to get the sentiment classes
filename = "synData.csv"
df = pd.read_csv(filename, names=["sentiment", "text"], encoding="utf-8", encoding_errors="replace")

# Get unique sentiments from the CSV file
sentiments = sorted(df.sentiment.unique())
sentiment_string = "\n ".join(sentiments)

# Disclaimer about the classes
st.write(f"The bot is able to detect the following text categories: {', '.join(sentiments)}")

# Function to simulate text analysis
def random_response():
    return "This is a random response. The actual analysis is best performed locally."

# Streamlit Chat Interface
st.write("### Enter text to analyze:")

# User input
user_input = st.text_area("Your text here...")

if user_input:
    with st.spinner("Analyzing sentiment..."):
        # Simulate a random response
        sentiment_detected = random.sample(sentiments,1)[0]

        # Display the result
        st.write(f"Detected text category: **{sentiment_detected}**")
        st.write("This is a random response. The actual analysis is best performed locally.")
