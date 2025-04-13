import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    if text_to_analyse.strip() == '':
        

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()

        # return all key values with None for server response to blank entry
        if response.status_code == 400:
            return { 
                "anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None,
                "dominant_emotion": None 
                }

        result = json.loads(response.text)
        emotionPredictions = result['emotionPredictions']
        emotion_dict = {}

        for item in emotionPredictions:
            if 'emotion' in item:
                emotions = item['emotion']
                score = 0
                for key,value in emotions.items():
                    emotion_dict[key] = value
                    if (score < value):
                        dominant_emotion = key
                        score = value
                emotion_dict['dominant_emotion'] = dominant_emotion

        return emotion_dict
    except requests.exceptions.RequestException as e:
        print("Error calling the API:", e)
        return None
