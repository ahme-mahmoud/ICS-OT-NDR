<p align="center">
  <img 
    src="assets/logo0.png"
    alt="ICS/OT Network Detection and Response"
    width="600"
  />
</p>

<h1 align="center">ICS/OT Network Detection and Response</h1>

<p align="center">
  <strong>
    Industrial Cyber Security • Anomaly Detection • Scan & Attack Detection
  </strong>
</p>

---

# 🚨 ICS/OT Network Detection and Response (ML-Based)

## 📌 Project Overview

This project implements a **Machine Learning–Based Network Detection and Response (NDR)** system for **Industrial Control Systems (ICS)** and **Operational Technology (OT)** environments.

Unlike traditional signature-based IDS solutions, this system relies on **behavior-based anomaly detection**, which is more suitable for industrial networks where:

- Normal behavior is stable and predictable  
- Attack samples are limited or unknown  
- Availability and safety are critical  

The system is designed to detect **network scans, anomalies, and real cyber attacks** targeting **PLC-based industrial networks**.

---

## 🎯 Problem Statement

ICS/OT networks (power plants, substations, water treatment facilities, manufacturing systems) face unique security challenges:

- Legacy industrial protocols without authentication or encryption  
- Limited visibility into OT network traffic  
- Highly imbalanced datasets (normal traffic ≫ attacks)  
- Traditional firewalls and rule-based IDS cannot detect zero-day attacks  
- Downtime is unacceptable due to safety and operational risks  

---

## 💡 Solution Approach

To address these challenges, this project implements a **two-stage ML-based detection pipeline**:

### 1️⃣ Anomaly Detection  
Learns **only normal behavior** and flags any deviation as suspicious.

### 2️⃣ Attack Classification  
Classifies anomalous traffic into:
- **Network Scans** (e.g., Nmap reconnaissance)
- **Real Attacks** (Hijacking, MAC flooding, TCPKill, etc.)

This architecture prioritizes **behavior deviation detection**, which is critical in ICS/OT environments.

---

## 🧠 Dataset

### Cyber4OT Dataset (2025)

This project uses the **Cyber4OT dataset**, a realistic and modern ICS/OT dataset containing:

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
- Realistic OT traffic patterns
- Highly imbalanced (very limited pure normal traffic)

This makes the dataset ideal for **anomaly detection in industrial networks**.

---

## 🏗️ System Architecture

<p align="center">
  <img 
    src="assets/system_architecture.png"
    alt="ICS/OT NDR System Architecture"
    width="750"
  />
</p>

```text
Network Traffic (PCAP / Live Capture)
              ↓
Feature Extraction (Flow-Level)
              ↓
Autoencoder (Trained on Normal Only)
              ↓
Is Anomaly?
       ↓                 ↓
    Normal        Scan / Attack Classifier
                         ↓
                   Scan OR Attack

```
---

The system first detects abnormal behavior using an **unsupervised autoencoder** trained only on normal traffic.  
If an anomaly is detected, the traffic is then passed to a **second-stage classifier** that determines whether the activity represents a **network scan** or a **real cyber attack**.

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
- Export results for backend & dashboard integration

---

## 🧪 Evaluation Metrics
- Accuracy
- Precision / Recall
- F1-score
- Confusion Matrix
- ROC-AUC

---

### 📊 Expected Performance (Based on Experiments)
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
- **Traffic Analysis:** Suricata / PCAP analysis
- **Model Serialization:** Joblib, Pickle
- **Backend:** Flask API
- **Dashboard:** Streamlit

---

## 🔌 Backend Integration

### Input Requirements
- flow_durat
- pkts_toserver
- pkts_toclient
- bytes_toserver
- bytes_toclient
- src_port
- dst_port

### Output
- normal
- scan
- attack

---

## 🚀 Future Work
- Real-time traffic ingestion
- Advanced dashboard analytics and alerting
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


