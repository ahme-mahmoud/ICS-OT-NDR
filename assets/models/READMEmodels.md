
NDR ML Pipeline – Anomaly → Scan / Attack Detection
Project Overview

This project implements a Network Detection & Response (NDR) machine learning pipeline using a two-stage detection architecture.

Due to the nature of the Cyber4OT dataset (which mainly contains Nmap scans and very limited real normal traffic), the solution is intentionally designed as:

Anomaly Detection (learning normal behavior only)

Attack Classification (Scan vs Real Attack)

This architecture is well-suited for ICS / OT networks, where detecting deviations from normal behavior is more important than traditional signature-based detection.

Architecture Overview
Network Traffic
      ↓
Feature Extraction
      ↓
Autoencoder (Trained on Normal Only)
      ↓
Is Anomaly?
   ↓         ↓
 Normal    Scan / Attack Classifier
               ↓
           Scan OR Attack

Stage 1 – Anomaly Detection (Autoencoder)
Concept

The autoencoder is trained only on pure normal traffic

Any deviation from learned normal behavior is flagged as an anomaly

Detection is based on reconstruction error

Required Files (models1 folder)

autoencoder_normal_only.keras

scaler_normal_only.pkl

normal_threshold.pkl

Inference Steps

Extract flow-level features

Apply scaling using scaler_normal_only.pkl

Pass data through the autoencoder

Compute reconstruction error

Compare the error with the threshold

Decision Rule

error ≤ threshold → Normal

error > threshold → Anomaly

Stage 2 – Scan vs Attack Classification
Concept

Only anomalous traffic is passed to this stage

A binary classifier distinguishes between:

Nmap / reconnaissance scans

Real attacks (Hijacking, TCPKill, MAC flooding, etc.)

Required Files (models1 folder)

scan_attack_model.pkl

scan_attack_scaler.pkl

Inference Steps

Take anomalous flows

Apply scaling using scan_attack_scaler.pkl

Predict using scan_attack_model.pkl

Output Labels

0 → Scan

1 → Attack

Final Output Labels
Condition	Final Label
Normal	normal
Anomaly + Scan	scan
Anomaly + Attack	attack
Backend Integration Requirements

The backend must send flow-level features in the same format and order used during training

The ML pipeline returns one label per flow:

normal

scan

attack

Required Input Features (in order)
flow_durat
pkts_toserver
pkts_toclient
bytes_toserver
bytes_toclient
src_port
dst_port
