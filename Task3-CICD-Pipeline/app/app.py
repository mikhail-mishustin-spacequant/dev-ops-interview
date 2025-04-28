from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from CI/CD Pipeline Demo App!",
        "version": "1.0.0",
        "status": "running"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@app.route('/api/data')
def get_data():
    # This endpoint would typically fetch data from a database
    # For demo purposes, we're returning static data
    return jsonify({
        "items": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
