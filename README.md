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
│── data/                     # Datasets (thermal, underwater images)
│   ├── raw/                  # Unprocessed data
│   ├── processed/            # Preprocessed data
│── models/                   # Saved trained models
│── notebooks/                # Jupyter notebooks for experiments
│── src/                      # Core source code
│   ├── __init__.py           # Package initializer
│   ├── components/           # Core ML pipeline components
│   │   ├── __init__.py
│   │   ├── data_ingestion.py # Fetch & preprocess data
│   │   ├── data_validation.py # Validate dataset integrity
│   │   ├── data_transformation.py # Feature engineering
│   │   ├── model_trainer.py  # Train YOLOv8 model
│   │   ├── model_evaluation.py # Evaluate model performance
│   │   ├── model_pusher.py   # Deploy model to cloud/edge
│   ├── pipelines/            # End-to-end ML workflows
│   │   ├── training_pipeline.py
│   │   ├── inference_pipeline.py
│   ├── services/             # API & streaming services
│   │   ├── __init__.py
│   │   ├── camera_stream.py  # Live camera feed processing
│   │   ├── api_service.py    # FastAPI-based inference service
│   ├── utils/                # Helper functions
│   │   ├── __init__.py
│   │   ├── main_utils.py
│   ├── config/               # Config files for easy parameter tuning
│   │   ├── config.yaml
│   │   ├── schema.yaml
│── tests/                    # Unit & integration tests
│── config.yaml               # Global configuration
│── requirements.txt          # Dependencies
│── README.md                 # Project documentation
│── Dockerfile                # Containerization for deployment
│── app.py                    # FastAPI-based inference server
│── setup.py                  # Installation script
│── pyproject.toml            # Modern Python project metadata
│── .dockerignore             # Files to exclude from Docker builds
│── demo.py                   # Quick demo script

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

