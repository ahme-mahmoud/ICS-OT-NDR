<p align="center">
  <img src="assets/logo0.png" alt="ICS/OT Network Detection and Response Logo" width="450"/>
</p>

<h1 align="center">ICS/OT Network Detection and Response</h1>

<p align="center">
  Industrial Cyber Security • Anomaly Detection • Scan & Attack Detection
</p>



# 🚨 ICS/OT Network Detection and Response (ML-Based)

## 📌 Project Overview

This project implements a **Machine Learning–Based Network Detection and Response (NDR)** system for **Industrial Control Systems (ICS)** and **Operational Technology (OT)** environments.

Unlike traditional signature-based IDS solutions, this system focuses on **behavior-based anomaly detection**, which is more suitable for industrial networks where:

- Normal behavior is stable and predictable  
- Attack samples are limited or unknown  
- Availability and safety are critical  

The solution is designed to detect **network scans, anomalies, and real cyber attacks** targeting industrial networks such as **PLC-based systems**.

---

## 🎯 Problem Statement

ICS/OT networks (power plants, substations, water treatment facilities, manufacturing systems) face unique security challenges:

- Legacy industrial protocols with no authentication or encryption  
- Limited visibility into OT network traffic  
- Highly imbalanced datasets (normal traffic ≫ attacks)  
- Traditional firewalls and rule-based IDS fail to detect unknown or zero-day attacks  
- Downtime is unacceptable due to safety and operational risks  

---

## 💡 Solution Approach

To address these challenges, this project implements a **two-stage ML-based detection pipeline**:

### 1️⃣ Anomaly Detection  
Learns **only normal behavior** and detects any deviation.

### 2️⃣ Attack Classification  
Classifies anomalous traffic into:
- **Network Scans** (e.g., Nmap)
- **Real Attacks** (Hijacking, MAC flooding, TCPKill, etc.)

This architecture is well-suited for ICS/OT environments, where detecting **abnormal behavior** is more important than matching predefined signatures.

---

## 🧠 Dataset

### Cyber4OT Dataset (2025)

This project uses the **Cyber4OT dataset**, a modern and realistic ICS/OT dataset containing:

- Real industrial network traffic  
- Normal operational behavior  
- Full attack scenarios, including:
  - Network reconnaissance (Nmap scans)
  - PLC connection disruption
  - PLC device hijacking
  - Modbus TCP–based attacks  

**Dataset Characteristics:**
- Over **4.25 million packets**
- **96 PCAP files**
- Realistic OT traffic behavior
- Highly imbalanced (very limited pure normal traffic)

This makes the dataset ideal for **anomaly detection research** in ICS/OT environments.

---

## 🏗️ System Architecture

Network Traffic
↓
Feature Extraction (Flow-Level)
↓
Autoencoder (Trained on Normal Only)
↓
Is Anomaly?
↓ ↓
Normal Scan / Attack Classifier
↓
Scan OR Attack


---

## ⚙️ Machine Learning Models

### 1️⃣ Autoencoder – Anomaly Detection
- **Type:** Deep Learning (Unsupervised)
- **Training Data:** Pure normal traffic only
- **Detection Method:** Reconstruction error
- **Purpose:** Detect deviations from learned normal behavior
- **Strength:** Detects unknown and zero-day attacks

---

### 2️⃣ Scan vs Attack Classifier
- **Type:** Supervised ML classifier
- **Input:** Only anomalous flows
- **Output:** Scan or Real Attack
- **Purpose:** Reduce false alarms and provide meaningful attack context

---

## 📂 Project Pipeline

- PCAP traffic ingestion  
- Feature extraction (flow-level statistics)  
- Data cleaning and preprocessing  
- Model training (normal-only learning)  
- Threshold calculation for anomaly detection  
- Full dataset inference  
- Scan vs Attack classification  
- Export results for backend integration  

---

## 🧪 Evaluation Metrics

- Accuracy  
- Precision / Recall  
- F1-score  
- Confusion Matrix  
- ROC-AUC  

### Expected Performance (Based on Experiments)

| Model              | Expected Accuracy |
|--------------------|-------------------|
| Isolation Forest   | 70% – 85%         |
| Autoencoder        | 80% – 92%         |
| Two-Stage Pipeline | Up to ~95%        |

---

## 🛠️ Tools & Technologies

- **Programming:** Python  
- **ML Libraries:** Scikit-learn, TensorFlow / Keras  
- **Data Processing:** Pandas, NumPy  
- **Traffic Analysis:** Zeek / PCAP analysis  
- **Model Serialization:** Joblib, Pickle  
- **Visualization (Planned):** Streamlit  
- **Backend Integration (Planned):** Flask API  

---

## 🔌 Backend Integration

### Input Requirements

The backend must send **flow-level features** in the same format and order used during training:

1. `flow_durat`  
2. `pkts_toserver`  
3. `pkts_toclient`  
4. `bytes_toserver`  
5. `bytes_toclient`  
6. `src_port`  
7. `dst_port`  

### Output

The ML pipeline returns **one label per flow**:

- `normal`
- `scan`
- `attack`

---

## 🚀 Future Work

- Real-time traffic ingestion  
- Backend REST API for live detection  
- Interactive dashboard for alerts and analytics  
- Support for additional OT protocols (IEC-104, DNP3)  
- Ensemble and hybrid anomaly detection models  
- Deployment in real industrial testbeds  

---

## 📚 References

- Cyber4OT Dataset – SoftwareX (2025)  
- ICS/OT Security Research Literature  
- Anomaly Detection in Industrial Networks  
- NIST Cybersecurity Framework  
- IEC 62443 Industrial Security Standard  
