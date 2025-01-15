"""That application runs an emotion detector."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def emot_analyzer():
    """Return the result of the emotions of the text in string format."""
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    string_result = "For the given statement, the system response is "
    string_result += f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
    string_result += f"'fear': {result['fear']}, 'joy': {result['joy']} and "
    string_result += f"'sadness': {result['sadness']}. "
    string_result += f"The dominant emotion is {result['dominant_emotion']}."
    return string_result
@app.route("/")
def render_index_page():
    """Return the index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
