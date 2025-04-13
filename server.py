"""
This program to start server for Emotion Detection
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

## Initiate Flask app
app = Flask(__name__)

@app.route("/")
def home():
    """Define a route for the root URL ("/")
    Returns:
        The return value of the function.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def call_emotion():
    """Define a rourte for URL ("/emotionDetector")
    Returns:
        The emotion list of given text
    """
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    return result
