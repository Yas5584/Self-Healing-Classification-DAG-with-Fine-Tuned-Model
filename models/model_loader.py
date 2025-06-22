import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def load_model(model_path=r"C:\Users\ys136\Desktop\Generative AI\intern project 2\models\sentiment_data"):
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer

def predict_sentiment(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)
    
    with torch.no_grad():
        logits = model(**inputs).logits
    
    probabilities = torch.softmax(logits, dim=-1).squeeze()
    confidence, predicted_class = torch.max(probabilities, dim=-1)
    
    return {
        "label": model.config.id2label[predicted_class.item()],
        "confidence": confidence.item()
    }


