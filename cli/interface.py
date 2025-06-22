from utils.logger import log_event

def get_user_input():
    return input("\nEnter text for sentiment analysis (type 'exit' to quit): ")

def ask_clarification():
    return input("(y/n) or enter correct label: ").strip()

def display_result(state):
    # Determine final label source
    if "corrected_label" in state:
        final_label = state["corrected_label"]
        source = "user correction"
    elif "backup_prediction" in state:
        final_label = state["backup_prediction"]["label"]
        source = "backup model"
    else:
        final_label = state["prediction"]["label"]
        source = "initial prediction"
    
    print(f"\n[Result] Final Label: {final_label.upper()} (via {source})")
    return final_label


