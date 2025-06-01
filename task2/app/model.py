from transformers import pipeline

# Loading emotion-classification pre-trained model from HuggingFace
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

# Function with input text and returns dict of label with confidence  
def predict_emotion(text: str):
    results = classifier(text)[0]

    # Sort(descending) result by confidence score, pick highest score
    top_result = sorted(results, key=lambda x: x['score'], reverse=True)[0]
    
    # Returns a dictionary of top_result, its confidence score and all_scores for each label
    return {
        "label": top_result["label"],
        "confidence": round(top_result["score"], 2),
        "all_scores": results
    }
