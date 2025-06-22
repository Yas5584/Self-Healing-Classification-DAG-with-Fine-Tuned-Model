from utils.config import CONFIDENCE_THRESHOLD
from utils.logger import log_event

def confidence_check_node(state: dict) -> dict:
    confidence = state["prediction"]["confidence"]
    state["needs_fallback"] = confidence < CONFIDENCE_THRESHOLD
    
    if state["needs_fallback"]:
        # Print to console
        print(f"[ConfidenceCheckNode] Confidence too low ({confidence:.2%} < {CONFIDENCE_THRESHOLD:.2%}). Triggering fallback...")
        log_event("confidence_check", {
            "status": "below_threshold",
            "confidence": confidence,
            "threshold": CONFIDENCE_THRESHOLD
        })
    return state