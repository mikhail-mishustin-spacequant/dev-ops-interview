from flask import Flask, jsonify, request, render_template_string
import os
import json
import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Hard-coded credentials (security issue #1)
DB_USER = "admin"
DB_PASSWORD = "super_secret_password123"
API_KEY = "1234567890abcdef"

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Security Demo Application!",
        "status": "running"
    })

# Insecure template rendering (security issue #2)
@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    template = f'''
    <h1>Hello, {name}!</h1>
    <p>Welcome to our application.</p>
    '''
    return render_template_string(template)

# Command injection vulnerability (security issue #3)
@app.route('/ping')
def ping():
    host = request.args.get('host', 'localhost')
    # Vulnerable command execution
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return jsonify({
        "command": f"ping -c 1 {host}",
        "result": result.decode('utf-8')
    })

# Insecure data handling (security issue #4)
@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.get_json()
    filename = data.get('filename', 'data.json')
    content = data.get('content', {})
    
    # Insecure file handling
    with open(filename, 'w') as f:
        json.dump(content, f)
    
    return jsonify({
        "status": "success",
        "message": f"Data saved to {filename}"
    })

# Exposed sensitive information (security issue #5)
@app.route('/debug')
def debug():
    return jsonify({
        "environment": dict(os.environ),
        "db_credentials": {
            "user": DB_USER,
            "password": DB_PASSWORD
        },
        "api_key": API_KEY
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == '__main__':
    # Insecure settings (security issue #6)
    app.run(host='0.0.0.0', port=8080, debug=True)
