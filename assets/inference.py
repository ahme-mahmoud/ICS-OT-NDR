import numpy as np
import joblib
import tensorflow as tf

# =========================
# Load Models & Artifacts
# =========================
AUTOENCODER_PATH = "ML/models/Anomaly Detection/autoencoder_normal_only.keras"
NORMAL_SCALER_PATH = "ML/models/Anomaly Detection/scaler_normal_only.pkl"
NORMAL_THRESHOLD_PATH = "ML/models/Anomaly Detection/normal_threshold.pkl"

SCAN_ATTACK_MODEL_PATH = "ML/models/Scan vs Attack Classification/scan_attack_model.pkl"
SCAN_ATTACK_SCALER_PATH = "ML/models/Scan vs Attack Classification/scan_attack_scaler.pkl"

autoencoder = tf.keras.models.load_model(AUTOENCODER_PATH)
normal_scaler = joblib.load(NORMAL_SCALER_PATH)
normal_threshold = joblib.load(NORMAL_THRESHOLD_PATH)

scan_attack_model = joblib.load(SCAN_ATTACK_MODEL_PATH)
scan_attack_scaler = joblib.load(SCAN_ATTACK_SCALER_PATH)

# =========================
# Feature Order (IMPORTANT)
# =========================
FEATURES = [
    "flow_durat",
    "pkts_toserver",
    "pkts_toclient",
    "bytes_toserver",
    "bytes_toclient",
    "src_port",
    "dst_port"
]

# =========================
# Prediction Function
# =========================
def predict_flow(flow_dict):
    """
    Input:
        flow_dict (dict):
        {
            "flow_durat": float,
            "pkts_toserver": int,
            "pkts_toclient": int,
            "bytes_toserver": int,
            "bytes_toclient": int,
            "src_port": int,
            "dst_port": int
        }

    Output:
        dict:
        {
            "label": "normal" | "scan" | "attack",
            "reconstruction_error": float
        }
    """

    # ---- Convert input to numpy array
    x = np.array([[flow_dict[f] for f in FEATURES]])

    # =========================
    # Stage 1: Anomaly Detection
    # =========================
    x_scaled = normal_scaler.transform(x)
    x_reconstructed = autoencoder.predict(x_scaled, verbose=0)

    reconstruction_error = float(
        np.mean(np.square(x_scaled - x_reconstructed))
    )

    if reconstruction_error <= normal_threshold:
        return {
            "label": "normal",
            "reconstruction_error": reconstruction_error
        }

    # =========================
    # Stage 2: Scan vs Attack
    # =========================
    x_attack_scaled = scan_attack_scaler.transform(x)
    pred = scan_attack_model.predict(x_attack_scaled)[0]

    label = "scan" if pred == 0 else "attack"

    return {
        "label": label,
        "reconstruction_error": reconstruction_error
    }
