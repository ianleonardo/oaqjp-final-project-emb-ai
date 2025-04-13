from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

## Initiate Flask app
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def home():
    return render_template('index.html')

## Define a rourte for URL ("/emotionDetector")
@app.route("/emotionDetector")
def emotionDetector():
    textToAnalyze = request.args.get("textToAnalyze")
    result = emotion_detector(textToAnalyze)
    
    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    else:
        return result
