# SentimentAnalyzerProject

**Try it!!** -> [Text Sentiment Analyzer](https://sentimentanalyzerproject.onrender.com)

This project is a sentiment analyzer that uses a Flask API to determine the emotional polarity of text entered by the user through a web interface. It uses the `vaderSentiment` library to classify sentiment as positive, negative, or neutral.

## Key Features

- **VADER-based sentiment analysis:** Uses the `SentimentIntensityAnalyzer` from the `vaderSentiment` library to analyze text polarity.
- **Interactive web interface:** Allows users to enter text through a web form.
- **Flask API:** Exposes an `/emotionDetector` endpoint to perform sentiment analysis.
- **Real-time results:** Displays the dominant sentiment of the analyzed text directly on the web page.
- **Deployment-ready:** Includes a `render.yaml` file to facilitate deployment on the Render platform.

## How to Use

1. Clone the repository:
```bash
git clone https://github.com/Nicolakorff/SentimentAnalyzerProject
cd SentimentAnalyzerProject
```
3. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate # On Linux/macOS
venv\Scripts\activate # On Windows
```
5. Install dependencies:
```bash
pip install -r requirements.txt
```
7. Run the Flask application locally:
```bash
python app.py
This will start the Flask server at http://127.0.0.1:5000/.
```
5. **Open the web interface:** Go to `http://127.0.0.1:5000/` in your web browser.
9. **Enter the text to analyze:** In the text box provided, type the phrase or text whose sentiment you want to analyze.
10. **Run the analysis:** Click the "Run Sentiment Analysis" button.
11. **View the result:** The dominant sentiment of the analyzed text (Positive, Negative, or Neutral) will be displayed in the "Result of Sentiment Analysis" section.
12. **Run the unit tests:**
```bash
python test_emotion_detection.py
```
This will run the tests defined in `test_emotion_detection.py` to verify the functionality of the emotion detector.

## Technologies Used

- **Python:** The core programming language.
- **Flask:** A web microframework for Python used to build the API and serve the web interface.
- **vaderSentiment:** A lexical- and rule-based NLP library specifically tuned for sentiment analysis on social media (implemented in `EmotionDetection/emotion_detection.py`).
- **HTML:** For the web page structure (`templates/index.html`).
- **CSS (Bootstrap):** For the styling and presentation of the web interface (included via CDN in `templates/index.html`).
- **JavaScript:** For client-side interactivity (`static/mywebscript.js`), sending the analysis request to the Flask API and updating the page with the response.
- **Gunicorn:** A WSGI HTTP server for serving the Flask application in a production environment (configured in `render.yaml`).
- **Render:** A cloud hosting platform used to deploy the application (configured via `render.yaml`).
- **unittest:** The Python unit testing framework used for testing in `test_emotion_detection.py`.

## Upcoming Improvements

- Support for analyzing the sentiment of multiple texts simultaneously.
- More detailed display of polarity scores (positive, negative, neutral, composite).
- Option to choose different sentiment analysis models.
- Batch sentiment analysis by uploading text files.
- Improved user interface and user experience.

## Contributions

Contributions to this project are welcome. If you have ideas for improving the app or have found a bug, please feel free to open an issue or submit a pull request.

## Author

Nicola Korff [My Github](https://github.com/Nicolakorff/)

## License

MIT License


<img width="799" alt="Captura de pantalla 2025-04-21 a las 23 00 40" src="https://github.com/user-attachments/assets/b2fa5346-d9e6-4549-806e-1fad97cbf7f7" />
