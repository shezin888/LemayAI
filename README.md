# Task 2: Emotion Classification API

## Model Used from Hugging Face

- **Model**: [`j-hartmann/emotion-english-distilroberta-base`](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)
- **Description**: Multi-class emotion classification of English text (e.g., joy, sadness, anger, fear).
- **Why this Model?**: I chose this model because it has real world applications in various domains. Its clear emotion label predictions make it useful for both  technical and non-technical users. One practical use case is that it can be integrated into commercial chatbot systems to analyze user's emotion tone from conversation This allows business to have an indirect feedback, helping them to improve their services. 

---

## Requirements

- Python 3.10 (running `test.ipynb`)
- Docker 
- Docker Compose 
- Platform: Cross-platform (Linux, macOS, Windows via Docker)

---

## How to Run the App

```bash
git clone <url>
cd task2
docker compose up
```
After that:
- Visit http://localhost:8000 to access the API.
- Use http://localhost:8000/docs for Swagger UI (default FastAPI UI).
- Use http://localhost:8000/ui to test via the HTML form (simple UI).
- Open `test.ipynb` to send parallel POST requests and visualize results.

---

## Live Demo: Deployed via Hugging Face Spaces

Check it out  👉 [**Here**  ](https://huggingface.co/spaces/shezin/LemayAI_Task2)

---

## Top Features

- Containerized API using FastAPI + Uvicorn
- Supports multi-threaded parallel requests

---

## Citation

This project uses the following model from Hugging Face:
> Hartmann, Jochen. *Emotion English DistilRoBERTa-base*. 2022.  
> Available at: [https://huggingface.co/j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)
