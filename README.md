Self-Healing-Classification-DAG-with-Fine-Tuned-Model

This project implements a robust sentiment analysis system with self-healing capabilities using LangGraph workflows. The system classifies text sentiment while incorporating a fallback mechanism for low-confidence predictions through user clarification or backup models.

Key Features
🧠 Fine-tuned transformer model for sentiment analysis

🔄 Self-healing workflow with confidence-based fallback

💬 Interactive CLI for user clarification

📊 Structured logging and visualization

🛡️ Backup model integration for robust predictions

📈 Confidence tracking and fallback statistics

Requirements
Python 3.10+

GPU recommended for training (CPU sufficient for inference)
1.Installation
Clone the repository:
git clone 

2.Create and activate virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3.Install dependencies:
pip install -r requirements.txt

4.Set up environment variables:
cp .env.example .env

Usage
1. Fine-tune the Model (Optional)
python -m models.fine_tuning

2. Run the Sentiment Analysis System
python main.py

3. Interact with the System
text
Enter text for sentiment analysis (type 'exit' to quit): The movie was painfully slow and boring

[InferenceNode] Predicted label: POSITIVE | Confidence: 54.20%
[ConfidenceCheckNode] Confidence too low (0.5420 < 0.7000). Triggering fallback...
[FallbackNode] Was this actually a NEGATIVE review?
(y/n) or enter correct label: y
[FallbackNode] User confirmed: NEGATIVE

[Result] Final Label: NEGATIVE (via user correction)
Project Structure
text
sentiment-selfhealing/
├── models/                  # Model-related code
│   ├── fine_tuning.py       # Fine-tuning logic
│   └── model_loader.py      # Model loading/prediction
├── nodes/                   # LangGraph nodes
│   ├── inference_node.py    # Prediction node
│   ├── confidence_check.py  # Confidence evaluation
│   └── fallback_node.py     # Fallback handling
├── workflow/                # DAG orchestration
│   └── build_graph.py       # LangGraph assembly
├── cli/                     # User interface
│   ├── interface.py         # Input/output handling
│   └── visualization.py     # Bonus stats/charts
├── utils/                   # Shared utilities
│   ├── logger.py            # Structured logging
│   └── config.py            # Configuration management
├── data/                    # Sample datasets
├── logs/                    # Execution logs
├── sentiment_model/         # Fine-tuned model (generated)
├── main.py                  # Entry point
├── requirements.txt         # Dependencies
├── .env                     # Environment configuration
└── README.md                # This file
Configuration
Edit the .env file to customize system behavior:

env
# Confidence threshold for fallback (0-1)
CONFIDENCE_THRESHOLD=0.7

# Backup model for fallback scenarios
BACKUP_MODEL_NAME=facebook/bart-large-mnli

# Path to fine-tuned model
MODEL_PATH=sentiment_model

Demo-

Bonus Features
Backup model integration for zero-shot classification

Confidence trend visualization:
https://docs/confidence_chart.png

Fallback resolution statistics:
https://docs/fallback_stats.png

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Hugging Face for transformer models

LangChain for workflow orchestration

IMDB dataset for sentiment analysis


