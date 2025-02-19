# **InfraDeep: AI-Powered Thermal & Underwater Object Detection**

## **🔍 Overview**
InfraDeep is an advanced AI-powered vision system that leverages **thermal imaging** and **underwater object detection** to enhance security, surveillance, and marine exploration. This project integrates state-of-the-art **computer vision** and **deep learning** techniques to detect objects in challenging environments where traditional cameras fail.

## **🌟 Key Features**
✅ **Thermal Object Detection:** Identifies humans, vehicles, and intruders using infrared imaging.
✅ **Underwater Object Recognition:** Detects marine life, submerged objects, and wreckage.
✅ **Real-time Processing:** Uses **YOLOv8 + OpenCV** for fast and efficient detection.
✅ **Multi-Environment Adaptability:** Can process both live feeds and static images.
✅ **API for Integration:** Deployable as a **FastAPI-based inference server**.
✅ **Edge Deployment Ready:** Can run on **Raspberry Pi, Jetson Nano, or cloud servers**.

## **🛠 Tech Stack**
- **Deep Learning:** YOLOv8, PyTorch
- **Computer Vision:** OpenCV, MediaPipe
- **Infrared & Underwater Datasets:** Custom and publicly available datasets
- **Deployment:** FastAPI, Docker
- **Hardware Support:** Compatible with **FLIR thermal cameras**, **Raspberry Pi**, and standard webcams

---

## **📁 Project Structure**
```
InfraDeep/
│── components/                  # Core ML pipeline components
│   ├── data_ingestion.py        # Data ingestion logic
│   ├── data_validation.py       # Validate input data
│   ├── data_transformation.py   # Transform data for modeling
│   ├── model_trainer.py         # Train the ML model
│   ├── model_evaluation.py      # Evaluate trained models
│   ├── model_pusher.py          # Deploy the trained model
│
│── configuration/               # Configuration management
│   ├── mongo_db_connection.py   # MongoDB connection settings
│
│── cloud_storage/               # Cloud storage utilities
│   ├── aws_storage.py           # AWS S3 storage management
│
│── data_access/                 # Data access layer
│   ├── project_data.py          # Manage datasets
│
│── entity/                      # Entity definitions
│   ├── config_entity.py         # Config schema definitions
│   ├── artifact_entity.py       # Data artifact tracking
│   ├── estimator.py             # Model estimation logic
│   ├── s3_estimator.py          # S3-based model management
│
│── exception/                   # Custom exception handling
│
│── logger/                      # Logging setup
│
│── mlflow_logs/                 # MLflow tracking
│   ├── tracking.py              # MLflow experiment tracking
│
│── pipeline/                    # ML pipelines
│   ├── training_pipeline.py     # Model training pipeline
│   ├── prediction_pipeline.py   # Model inference pipeline
│
│── utils/                       # Utility scripts
│   ├── main_utils.py            # Helper functions
│
│── config/                      # Configuration files
│   ├── model.yaml               # Model parameters
│   ├── schema.yaml              # Data schema
│
│── app.py                       # FastAPI-based inference server
│── requirements.txt              # Dependencies
│── Dockerfile                    # Containerization setup
│── .dockerignore                 # Docker ignore files
│── demo.py                        # Sample script
│── setup.py                       # Installation script
│── pyproject.toml                 # Modern package management

---

## **🚀 Getting Started**
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/InfraDeep.git
cd InfraDeep
```

### **2. Set Up Virtual Environment**
```bash
python -m venv infradeep_env
source infradeep_env/bin/activate  # Mac/Linux
infradeep_env\Scripts\activate     # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Train the Model**
```bash
python src/train.py --dataset data/thermal_and_underwater --epochs 50
```

### **5. Run Inference on an Image**
```bash
python src/inference.py --image test_image.jpg
```

### **6. Start the API Server**
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

---

## **📊 Dataset Sources**
- **Thermal Images:** [FLIR Thermal Dataset](https://www.flir.com/oem/adas/adas-dataset-form/)
- **Underwater Images:** [Marine Object Detection Dataset](https://www.kaggle.com/datasets)

---

## **🛠 Future Enhancements**
🔹 **Sign Language Recognition** – Expanding gesture detection for accessibility.
🔹 **Multi-Sensor Fusion** – Combining LiDAR, thermal, and standard cameras.
🔹 **Reinforcement Learning** – Adaptive AI models for dynamic environments.
🔹 **Mobile Deployment** – Optimize for smartphones and edge devices.

---

## **👨‍💻 Contributing**
We welcome contributions! Feel free to **fork, submit PRs, or open issues** for improvements.

### **🌟 Star the Repo & Stay Updated!** ⭐
If you find **InfraDeep** useful, consider giving it a star on GitHub! 🚀

