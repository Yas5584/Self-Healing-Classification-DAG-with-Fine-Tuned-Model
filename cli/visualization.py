import matplotlib.pyplot as plt
import numpy as np
from utils.logger import parse_logs
import os
from dotenv import load_dotenv
load_dotenv()
def generate_confidence_chart(logs,y=os.getenv("CONFIDENCE_THRESHOLD")):
    confidences = [log['data']['confidence'] for log in logs if 'prediction' in log['event']]
    
    plt.figure(figsize=(10, 5))
    plt.plot(confidences, 'bo-', label='Confidence Score')
    plt.axhline(y=y, color='r', linestyle='-', label='Confidence Threshold')
    plt.title('Prediction Confidence Over Time')
    plt.xlabel('Input Sequence')
    plt.ylabel('Confidence Score')
    plt.legend()
    plt.savefig('confidence_chart.png')
    print("Saved confidence_chart.png")

def generate_fallback_stats(logs):
    fallbacks = [log for log in logs if log['event'] == 'fallback']
    actions = [log['data']['action'] for log in fallbacks]
    
    counts = {
        'User Correction': actions.count('user_correction'),
        'Backup Model': actions.count('used_backup_model')
    }
    
    plt.figure(figsize=(8, 8))
    plt.pie(
        counts.values(), 
        labels=counts.keys(), 
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title('Fallback Resolution Methods')
    plt.savefig('fallback_stats.png')
    print("Saved fallback_stats.png")