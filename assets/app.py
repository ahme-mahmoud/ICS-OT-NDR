from flask import Flask, request, jsonify
from inference import predict_flow

app = Flask(__name__)

# =========================
# Health Check
# =========================
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "ICS/OT Network Detection & Response API",
        "status": "running"
    })

# =========================
# Prediction Endpoint
# =========================
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Required input features
        required_fields = [
            "flow_durat",
            "pkts_toserver",
            "pkts_toclient",
            "bytes_toserver",
            "bytes_toclient",
            "src_port",
            "dst_port"
        ]

        # ---- Validation
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "status": "error",
                    "message": f"Missing field: {field}"
                }), 400

        # ---- Run ML pipeline
        result = predict_flow(data)

        return jsonify({
            "status": "success",
            "prediction": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


# =========================
# Run Server
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
