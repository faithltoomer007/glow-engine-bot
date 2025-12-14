from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    print("🔥 New Glow Engine Signal Received")
    print(data)

    # Extract fields (optional for now)
    symbol = data.get("symbol")
    entry_type = data.get("entry_type")
    entry_price = data.get("entry_price")
    tp_price = data.get("tp_price")
    sl_price = data.get("sl_price")

    timestamp = datetime.datetime.now().isoformat()

    return jsonify({"status": "success", "received_at": timestamp}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
