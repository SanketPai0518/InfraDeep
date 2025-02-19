import os
from logger import logging
from pathlib import Path

# Project Name
project_name = "InfraDeep"

# Define directory structure
list_of_files = [
    f"{project_name}/__init__.py",
    
    # Data pipeline
    f"{project_name}/data/__init__.py",
    f"{project_name}/data/ingestion.py",
    f"{project_name}/data/transformation.py",
    f"{project_name}/data/validation.py",
    f"{project_name}/data/thermal/.gitkeep",
    f"{project_name}/data/underwater/.gitkeep",

    # Model pipeline
    f"{project_name}/models/__init__.py",
    f"{project_name}/models/trainer.py",
    f"{project_name}/models/evaluation.py",
    f"{project_name}/models/registry.py",  # Stores trained models

    # MLflow tracking
    f"{project_name}/mlflow_logs/__init__.py",
    f"{project_name}/mlflow_logs/tracking.py",  # Handles experiment logging

    # Notebooks
    f"{project_name}/notebooks/__init__.py",
    
    # Source Code
    f"{project_name}/src/__init__.py",
    f"{project_name}/src/train.py",
    f"{project_name}/src/inference.py",
    f"{project_name}/src/preprocess.py",
    f"{project_name}/src/camera_stream.py",
    f"{project_name}/src/utils.py",

    # Pipelines
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    # Tests
    f"{project_name}/tests/__init__.py",
    f"{project_name}/tests/test_train.py",
    f"{project_name}/tests/test_inference.py",

    # Config and dependencies
    "config.yaml",
    "requirements.txt",
    "README.md",
    "Dockerfile",
    "app.py",
    "setup.py"
]

# Create directories and files
for file_path in list_of_files:
    filepath = Path(file_path)
    filedirectory, filename = os.path.split(filepath)

    if filedirectory:
        os.makedirs(filedirectory, exist_ok=True)
        logging.info(f"Created directory: {filedirectory}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as file:
            pass
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")

logging.info("InfraDeep project structure initialized successfully!")
