from cli.interface import ask_clarification
from utils.logger import log_event

def fallback_node(state: dict) -> dict:
    if not state.get("needs_fallback", False):
        return state
    
    predicted_label = state["prediction"]["label"]
    
    # Generate intelligent clarification question
    if predicted_label == "positive":
        question = f"Was this actually a NEGATIVE review?"
    else:
        question = f"Was this actually a POSITIVE review?"
    
    print(f"[FallbackNode] {question}")
    
    # Get user response
    user_response = ask_clarification()
    
    # Process response
    if user_response.lower() in ["y", "yes"]:
        corrected_label = "negative" if predicted_label == "positive" else "positive"
        print(f"[FallbackNode] User confirmed: {corrected_label.upper()}")
    elif user_response.lower() in ["n", "no"]:
        corrected_label = predicted_label
        print(f"[FallbackNode] User confirmed original prediction: {corrected_label.upper()}")
    else:
        corrected_label = user_response
        print(f"[FallbackNode] User provided new label: {corrected_label.upper()}")
    
    state["corrected_label"] = corrected_label
    log_event("fallback", {"action": "user_correction", "response": user_response})
    
    return state