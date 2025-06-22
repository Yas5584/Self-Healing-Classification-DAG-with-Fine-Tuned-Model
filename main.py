import sys
import os
import os
from workflow.build_graph import build_workflow
from models.model_loader import load_model
from cli.interface import get_user_input, display_result
from cli.visualization import generate_confidence_chart, generate_fallback_stats
from utils.logger import log_event, parse_logs
from utils.config import MODEL_PATH

def main():
    # Load model
    model, tokenizer = load_model(MODEL_PATH)
    
    # Build workflow
    workflow = build_workflow(model, tokenizer)
    
    print("Sentiment Analysis System with Self-Healing")
    print("------------------------------------------")
    
    while True:
        text = get_user_input()
        if text.lower() in ['exit', 'quit']:
            break
        
        # Initialize state
        state = {"text": text}
        
        try:
            # Execute workflow
            state = workflow.invoke(state)
            
            # Display and log result
            final_label = display_result(state)
            log_event("final_decision", {
                "text": text,
                "final_label": final_label,

            })
            
        except Exception as e:
            log_event("error", {
                "text": text,
                "error": str(e)
            })
            print(f"Error processing input: {e}")
    
    # Generate bonus visualizations
    try:
        logs = parse_logs()
        generate_confidence_chart(logs)
        generate_fallback_stats(logs)
    except Exception as e:
        print(f"Couldn't generate visualizations: {e}")

if __name__ == "__main__":
    main()