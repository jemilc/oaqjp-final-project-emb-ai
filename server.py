from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def emot_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    
    # Check if input is blank or None
    if not text_to_analyze or text_to_analyze.strip() == "":
        # Return 400 status code and a response with None values for all keys
        response = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        return jsonify(response), 400

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if "dominant_emotion" is None
    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!", 400

     # Extract the dominant emotion
    dominant_emotion = response["dominant_emotion"]

    # Build the response string
    emotion_scores = ', '.join([f"'{emotion}': {score}" for emotion, score in response.items() if emotion != "dominant_emotion"])
    output = f"For the given statement, the system response is {emotion_scores}. The dominant emotion is {dominant_emotion}."

    return output

    
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
