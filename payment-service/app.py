from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="UP"), 200

@app.route("/payments")
def payments():
    return jsonify({
        "service": "payment-service",
        "payments": [
            {"id": 103, "amount": 500},
            {"id": 102, "amount": 1200}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)

