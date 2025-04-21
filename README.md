# SentimentAnalyzerProject

**Try it here!!** -> https://sentimentanalyzerproject.onrender.com

This project is a web application that allows users to enter text and detect its overall sentiment (Positive, Negative, or Neutral) using the VADER (Valence Aware Dictionary and Sentiment Reasoner) library in Python.

<img width="799" alt="Captura de pantalla 2025-04-21 a las 23 00 40" src="https://github.com/user-attachments/assets/b2fa5346-d9e6-4549-806e-1fad97cbf7f7" />

## Project Structure

- app.py # Main logic of the Flask application
- EmotionDetection/
  - init.py # Initializes the directory as a Python package
  - emotion_detection.py # Contains the function to perform sentiment analysis with VADER
- requirements.txt # List of Python dependencies
- static/
  - mywebscript.js # JavaScript code for interaction with the frontend
- templates/
  - index.html # Web application user interface
- render.yaml # Configuration for deployment to Render
- README.md # This file
- test_emotion_detection.py # Unit tests for the sentiment detection feature

## How It Works

1. The user accesses the web page (`index.html`) through their browser.
2. They enter the text they want to analyze in the provided text area.
3. They click the "Run Sentiment Analysis" button.
4. The JavaScript code (`mywebscript.js`) sends the entered text to the `/emotionDetector` path of the Flask application (`app.py`).
5. The Flask application receives the text and uses the `emotion_detector` function (defined in `EmotionDetection/emotion_detection.py`) to analyze the sentiment using the VADER library.
6. The `emotion_detector` function returns the overall sentiment (Positive, Negative, or Neutral).
7. The Flask application sends this result back to the browser.
8. The JavaScript code updates the web page (`index.html`) to display the detected sentiment.

## Deployment

This application is configured to be easily deployed to [Render](https://render.com/). The `render.yaml` file contains the necessary configuration.
