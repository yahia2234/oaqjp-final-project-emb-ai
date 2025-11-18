"""
Flask application for detecting emotions from user text input.
Provides an endpoint to analyze emotions using the EmotionDetection package.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the home page with the input form.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_service():
    """
    Process the user's input text, run emotion detection, and return a formatted response.

    Returns:
        str: Formatted string containing emotion scores and dominant emotion,
             or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_response


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
