from flask import Flask, jsonify, request
import time
import logging
import random
import os
from prometheus_client import Counter, Histogram, start_http_server

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Initialize the Flask application
app = Flask(__name__)

# Set up Prometheus metrics
REQUEST_COUNT = Counter('app_request_count', 'Application Request Count', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Application Request Latency', ['method', 'endpoint'])

# Start Prometheus metrics server on port 8000
start_http_server(8000)

# Middleware to track metrics
@app.before_request
def before_request():
    request.start_time = time.time()
    logger.info(f"Received request: {request.method} {request.path} from {request.remote_addr}")

@app.after_request
def after_request(response):
    request_latency = time.time() - request.start_time
    REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()
    REQUEST_LATENCY.labels(request.method, request.path).observe(request_latency)
    
    logger.info(f"Request completed: {request.method} {request.path} - Status: {response.status_code} - Duration: {request_latency:.4f}s")
    return response

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Hello from the Monitoring Demo Application!",
        "status": "running"
    })

# Simulated API endpoint with variable latency
@app.route('/api/data')
def get_data():
    # Simulate variable response time
    latency = random.uniform(0.1, 0.5)
    time.sleep(latency)
    
    # Occasionally generate an error for monitoring demonstration
    if random.random() < 0.05:  # 5% error rate
        logger.error("Simulated server error occurred!")
        return jsonify({"error": "Internal Server Error"}), 500
    
    # Return mock data
    return jsonify({
        "items": [
            {"id": 1, "name": "Item 1", "value": random.randint(10, 100)},
            {"id": 2, "name": "Item 2", "value": random.randint(10, 100)},
            {"id": 3, "name": "Item 3", "value": random.randint(10, 100)}
        ],
        "timestamp": time.time()
    })

# High CPU usage simulation endpoint
@app.route('/simulate/cpu')
def simulate_cpu():
    logger.warning("CPU load simulation started")
    duration = min(int(request.args.get('duration', 10)), 30)  # Maximum 30 seconds
    
    end_time = time.time() + duration
    while time.time() < end_time:
        # Burn CPU for specified duration
        _ = [i**2 for i in range(100000)]
    
    logger.warning("CPU load simulation completed")
    return jsonify({
        "message": f"CPU load simulated for {duration} seconds",
        "status": "completed"
    })

# Memory leak simulation endpoint
@app.route('/simulate/memory')
def simulate_memory():
    logger.warning("Memory consumption simulation started")
    # This is just a simulation - in a real app we wouldn't want to do this
    size_mb = min(int(request.args.get('size', 10)), 50)  # Maximum 50 MB
    
    # Simulate memory allocation (this is temporary and will be garbage collected)
    temp_data = ' ' * (size_mb * 1024 * 1024)
    
    logger.warning(f"Allocated {size_mb}MB of memory temporarily")
    return jsonify({
        "message": f"Memory consumption simulated ({size_mb}MB)",
        "status": "completed"
    })

# Health check endpoint
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "uptime": time.time() - start_time
    })

if __name__ == '__main__':
    start_time = time.time()
    logger.info("Application starting up")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
