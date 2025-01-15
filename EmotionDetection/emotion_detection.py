import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector (text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } } # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request
    
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    response_data = json.loads(response.text) # Parse the JSON response

    # Extract emotion scores from the nested structure
    emotion_scores = response_data['emotionPredictions'][0]['emotion']
    
    # Find the emotion with the highest score
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Add the dominant emotion to the result
    emotion_scores['dominant_emotion'] = dominant_emotion
    
    return emotion_scores  # Return the response text from the API

