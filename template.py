import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
list_of_files = [
    "models/__init__.py",
    "models/fine_tuning.py",
    "models/model_loader.py",
    "nodes/__init__.py",
    "nodes/inference_node.py",
    "nodes/confidence_check.py",
    "nodes/fallback_node.py",
    "workflow/__init__.py",
    "workflow/build_graph.py",
    "cli/__init__.py",
    "cli/interface.py",
    "cli/visualization.py",
    "utils/__init__.py",
    "utils/logger.py",
    "utils/config.py",
    "main.py",
    "requirements.txt"
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for file {filename  }")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
    else:
        logging.info(f"{filename} is already exists")