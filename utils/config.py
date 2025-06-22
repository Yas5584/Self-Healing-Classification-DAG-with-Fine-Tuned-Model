import os
from dotenv import load_dotenv

load_dotenv()

# Configuration parameters
# CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", "0.9"))
# BACKUP_MODEL_NAME = os.getenv("BACKUP_MODEL_NAME", "facebook/bart-large-mnli")
# MODEL_PATH = r"C:\Users\ys136\Desktop\Generative AI\intern project 2\models\sentiment_data"

CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD"))
BACKUP_MODEL_NAME = os.getenv("BACKUP_MODEL_NAME")
MODEL_PATH=os.getenv("MODEL_PATH")