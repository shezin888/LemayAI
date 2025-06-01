from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from app.model import predict_emotion

# Initializing FastAPI app Obj
app = FastAPI()

# Expects JSON obj: {"text": "some text.."}
class TextInput(BaseModel):
    text: str

# root endpoint, with a status on API
@app.get("/")
def root():
    return {"message": "Emotion Classification API is running LIVE"}

# runs classifier on input and return result in JSON - used for test.ipynb results
@app.post("/predict")
def get_emotion(input_data: TextInput):
    result = predict_emotion(input_data.text)
    return result



# Simple UI HTML form for text input from browser
@app.get("/ui", response_class=HTMLResponse)
def form_ui():
    return """
    <html>
        <head><title>Emotion UI</title></head>
        <body>
            <h2>Enter text for emotion prediction:</h2>
            <form method="post" action="/ui">
                <textarea name="text" rows="4" cols="50" placeholder="Type here..."></textarea><br><br>
                <button type="submit">Predict</button>
            </form>
        </body>
    </html>
    """

# Runs classfier on text submitted via HTML form
@app.post("/ui", response_class=HTMLResponse)
def predict_ui(text: str = Form(...)):
    result = predict_emotion(text)

    # Builds HTML unordered list of all labels and scores 
    all_scores_html = "<ul style='font-size: 16px;'>"
    for score in result["all_scores"]:
        label = score["label"]
        confidence = round(score["score"] * 100, 2)
        all_scores_html += f"<li><strong>{label}</strong>: {confidence}%</li>"
    all_scores_html += "</ul>"

    return f"""
    <html>
        <head><title>Result</title></head>
        <body>
            <h2>Input:</h2>
            <p>{text}</p>

            <h2>Prediction:</h2>
            <p><strong>{result['label']}</strong> with confidence {round(result['confidence'] * 100, 2)}%</p>

            <h3>All Label Scores:</h3>
            {all_scores_html}

            <br><a href="/ui">Try another</a>
        </body>
    </html>
    """

