# Vehicle Insurance MLOps Pipeline

An **end-to-end MLOps project** that builds, trains, evaluates, and deploys a **Vehicle Insurance Prediction system** using modern ML engineering practices.

This project covers the **complete lifecycle**:

* Data ingestion from **MongoDB Atlas**
* Modular ML pipeline (validation, transformation, training, evaluation)
* Model versioning with **AWS S3**
* **FastAPI** application for prediction & training
* **Dockerized deployment**
* **CI/CD using GitHub Actions**
* Deployment on **AWS EC2**

The goal of this repository is to be **easy to understand**, **reproducible**, and **industry-oriented**.

---

## Problem Statement

Predict whether a customer will respond **Yes/No** to a vehicle insurance offer based on demographic and vehicle-related features.

Target column:

* `Response` → (Yes / No)

---

## High-Level Architecture

```
MongoDB Atlas
     ↓
Data Ingestion
     ↓
Data Validation
     ↓
Data Transformation
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Pusher (AWS S3)
     ↓
FastAPI App (Prediction + Training)
     ↓
Docker → CI/CD → AWS EC2
```

---

## Project Structure

```
Vehicle-Insurance-Data-Pipeline/
│
├── app.py                     # FastAPI entry point
├── Dockerfile                 # Docker configuration
├── .dockerignore
├── requirements.txt
├── pyproject.toml
├── setup.py
├── README.md
│
├── templates/                 # HTML templates
│   └── vehicledata.html
│
├── static/                    # CSS / static files
│   └── css/style.css
│
├── notebook/                  # EDA & MongoDB notebooks
│
├── src/
│   ├── constants/             # Global constants
│   ├── logger/                # Logging configuration
│   ├── exception/             # Custom exception handling
│   ├── configuration/         # MongoDB & AWS connections
│   ├── data_access/           # MongoDB data access layer
│   ├── entity/                # Config & artifact entities
│   ├── components/            # Pipeline components
│   ├── pipeline/              # Training & prediction pipelines
│   ├── utils/                 # Utility functions
│   └── aws_storage/            # S3 interaction logic
│
├── .github/workflows/
│   └── aws.yaml                # CI/CD pipeline
│
└── artifact/                   # Pipeline outputs (ignored in git)
```

---

## Step-by-Step Project Workflow

### 1️⃣ Project Setup

* Project template generated using `template.py`
* Local packages managed via `setup.py` and `pyproject.toml`
* Virtual environment created using Conda:

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
```

---

### 2️⃣ MongoDB Setup (Data Source)

* MongoDB Atlas cluster (M0 – Free Tier)
* Database user created
* Network access enabled: `0.0.0.0/0`
* Data pushed from notebook into MongoDB collection

Environment variable setup:

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>@..."
```

---

### 3️⃣ Logging & Exception Handling

* Centralized logging using Python `logging`
* Custom exception class with:

  * File name
  * Line number
  * Error message

Used across **all pipeline components**.

---

### 4️⃣ Data Ingestion

* Reads data from MongoDB Atlas
* Converts data into pandas DataFrame
* Stores raw data in **feature store**
* Splits data into `train.csv` and `test.csv`
* Saves outputs as timestamped artifacts

Artifact example:

```
artifact/<timestamp>/data_ingestion/
├── feature_store/data.csv
└── ingested/train.csv, test.csv
```

---

### 5️⃣ Data Validation

* Schema validation using `schema.yaml`
* Checks:

  * Column names
  * Data types
  * Missing values
* Generates validation report

---

### 6️⃣ Data Transformation

* Encoding categorical variables
* Scaling numerical features
* Saves:

  * Transformed train/test `.npy` files
  * Preprocessing object (`preprocessing.pkl`)

---

### 7️⃣ Model Training

* Algorithm: **RandomForestClassifier**
* Hyperparameters defined in constants
* Model trained on transformed data
* Evaluation metrics:

  * Accuracy
  * F1-score
  * Precision
  * Recall

A combined model object is created:

* Preprocessing + trained model

---

### 8️⃣ Model Evaluation & Model Pusher

* New model compared with existing model
* Threshold-based acceptance
* Accepted model pushed to **AWS S3**

AWS Setup:

* IAM User
* S3 Bucket (`my-model-mlopsproj`)

---

### 9️⃣ Prediction Pipeline & FastAPI App

* FastAPI provides:

  * `/` → Prediction UI
  * `/train` → Trigger training pipeline

* HTML + CSS UI

* Model loaded once (cached) for fast predictions

---

### 🔟 CI/CD Pipeline (GitHub Actions)

**CI (GitHub-hosted runner):**

* Build Docker image
* Push image to AWS ECR

**CD (Self-hosted runner on EC2):**

* Pull Docker image
* Stop old container
* Run new container

Secrets used:

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_DEFAULT_REGION`
* `ECR_REPO`
* `MONGODB_URL`

---

### 1️⃣1️⃣ Deployment on AWS EC2

* EC2 Ubuntu server
* Docker installed
* App runs inside container
* Port exposed: **5000**

Access application:

```
http://<EC2_PUBLIC_IP>:5000
```

Note: Some networks (like hostel Wi-Fi) may block custom ports.

---

## How to Run Locally

```bash
python app.py
```

Open browser:

```
http://localhost:5000
```

---

##  Key Learnings

* Modular MLOps pipeline design
* Artifact-based ML workflows
* Real-world CI/CD with self-hosted runners
* Debugging deployment & networking issues
* Production-style ML system design

---

## Future Improvements

* Nginx reverse proxy
* HTTPS
* Model monitoring
* Async inference

---

## Author

**Sadab Ali**
MLOps | Data Science | Machine Learning

---

⭐ If you find this project helpful, consider starring the repository!
