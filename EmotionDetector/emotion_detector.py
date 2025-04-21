from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def emotion_detector(text_to_analyse):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text_to_analyse)
    compound = vs['compound']

    if compound >= 0.05:
        dominant_emotion = 'Positive'
    elif compound <= -0.05:
        dominant_emotion = 'Negative'
    else:
        dominant_emotion = 'Neutral'

    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': dominant_emotion
    }

if __name__ == '__main__':
    print(emotion_detector("I am glad this happened"))
    print(emotion_detector("I am really mad about this"))
    print(emotion_detector("I feel disgusted just hearing about this"))
    print(emotion_detector("I am so sad about this"))
    print(emotion_detector("I am really afraid that this will happen"))
    print(emotion_detector("The weather is neutral today."))
