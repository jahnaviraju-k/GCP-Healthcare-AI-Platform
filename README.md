# 🌩️ Advanced Healthcare AI Platform on GCP

This project demonstrates how to build an **end-to-end AI-driven healthcare data platform** on **Google Cloud Platform (GCP)**.

## 🚀 Features
- ETL pipeline using **Dataflow** to load EHR data into BigQuery
- **Vertex AI** model for patient readmission risk prediction
- **Cloud Run API** serving predictions
- **Looker Studio / Streamlit Dashboard** for healthcare insights
- **Terraform IaC** for provisioning GCP resources

## 📊 Use Cases
- Patient readmission risk prediction
- Fraud detection on insurance claims
- IoT vitals streaming and anomaly detection

## 🏗️ GCP Services Used
- Cloud Storage, Pub/Sub, Dataflow
- BigQuery, Vertex AI, Cloud Run
- Looker Studio, IAM
- Terraform (Infrastructure as Code)

## ⚙️ How to Run Locally
```bash
pip install -r deploy/requirements.txt
python api/predict_api.py
```

