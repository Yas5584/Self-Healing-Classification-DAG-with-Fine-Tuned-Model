from models.model_loader import predict_sentiment
from utils.logger import log_event

def inference_node(state: dict, model, tokenizer) -> dict:
    text = state["text"]
    result = predict_sentiment(text, model, tokenizer)
    
    prediction = {
        "label": result["label"],
        "confidence": result["confidence"]
    }
    state["prediction"] = prediction
    
    # Print prediction to console
    print(f"[InferenceNode] Predicted label: {prediction['label'].upper()} | Confidence: {prediction['confidence']:.2%}")
    
    log_event("inference", {
        "text": text,
        "prediction": prediction
    })
    
    return state