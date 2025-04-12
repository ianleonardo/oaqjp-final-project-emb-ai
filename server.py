from flask import Flask
from flask import request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotionDetector():
    textToAnalyze = request.args.get("textToAnalyze")
    return emotion_detector(textToAnalyze)
