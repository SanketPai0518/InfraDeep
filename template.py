import os
from logger import logging
from pathlib import Path
project_name='InfraDeep'

# Define directory structure
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/data/__init__.py",
    f"{project_name}/data/thermal",
    f"{project_name}/data/underwater",
    f"{project_name}/models/__init__.py",
    f"{project_name}/notebooks/__init__.py",
    f"{project_name}/src/__init__.py",
    f"{project_name}/src/train.py",
    f"{project_name}/src/inference.py",
    f"{project_name}/src/preprocess.py",
    f"{project_name}/src/camera_stream.py",
    f"{project_name}/src/utils.py",
    f"{project_name}/tests/__init__.py",
    f"{project_name}/tests/test_train.py",
    f"{project_name}/tests/test_inference.py",
    "config.yaml",
    "requirements.txt",
    "README.md",
    "Dockerfile",
    "app.py",
    "setup.py"
]


for file_path in list_of_files:
    filepath    =   Path(file_path)
    filedirectory, filename = os.path.split(filepath)

    if filedirectory!="":
        os.makedirs(filedirectory, exist_ok=True)
        logging.info(f"Created directory: {filedirectory}")
        logging.info(f"Created file: {filename}")
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath, 'w') as file:
            pass
            logging.info(f"Created placeholder file: {filepath}")
    else:
                print("file is aldready present at{filepath}")

