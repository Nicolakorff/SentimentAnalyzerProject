from flask import Flask, render_template, request
from EmotionDetector.emotion_detector import emotion_detector

app = Flask(__name__) 

@app.route("/emotionDetector")
def emo_detector() :
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return f"The sentiment of the given statement is {dominant_emotion}."

@app.route("/")
def render_index_page() :
    return render_template('index.html')

if __name__ == "__main__" :
    app.run(host = "0.0.0.0", port = 5000, debug=True)
 
