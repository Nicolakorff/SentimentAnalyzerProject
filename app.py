from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector() :
    """
    It takes input text from user and send to appropriate function,
    then return response based on user text emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return f"The sentiment of the given statement is {dominant_emotion}."

@app.route("/")
def render_index_page() :
    """
    It starts server on defined server and port for development.
    """
    return render_template('index.html')

if __name__ == "__main__" :
    app.run(host = "0.0.0.0", port = 5000)
    
