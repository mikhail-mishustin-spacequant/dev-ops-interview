from flask import Flask, jsonify, request
import redis
import os
import psycopg2
import time

app = Flask(__name__)

# Configure Redis connection
redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port)

# Configure PostgreSQL connection
def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=os.environ.get('DB_HOST', 'db'),
                database=os.environ.get('DB_NAME', 'postgres'),
                user=os.environ.get('DB_USER', 'postgres'),
                password=os.environ.get('DB_PASSWORD', 'postgres')
            )
            return conn
        except psycopg2.OperationalError as e:
            retries -= 1
            print(f"Could not connect to database, retrying... ({retries} attempts left)")
            time.sleep(2)
    
    # If we failed to connect to database, still run app but with limited functionality
    return None

# Initialize the database
def init_db():
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS visits (id SERIAL PRIMARY KEY, timestamp VARCHAR(255));')
            conn.commit()
            cur.close()
            conn.close()
            print("Database initialized successfully")
        except Exception as e:
            print(f"Error initializing database: {e}")

# Home route
@app.route('/')
def home():
    # Increment visit counter in Redis
    visit_count = redis_client.incr('visit_count')
    
    # Store visit timestamp in Postgres
    conn = get_db_connection()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    
    if conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO visits (timestamp) VALUES (%s)', (timestamp,))
        conn.commit()
        cur.close()
        conn.close()
    
    return jsonify({
        "message": "Hello from Docker Compose Task!",
        "visit_count": visit_count,
        "timestamp": timestamp,
        "db_connected": conn is not None,
        "redis_connected": True
    })

# Health check endpoint
@app.route('/health')
def health():
    status = "healthy"
    db_status = "connected"
    redis_status = "connected"
    
    # Check Redis connection
    try:
        redis_client.ping()
    except:
        status = "degraded"
        redis_status = "disconnected"
    
    # Check DB connection
    conn = get_db_connection()
    if conn:
        conn.close()
    else:
        status = "degraded"
        db_status = "disconnected"
    
    return jsonify({
        "status": status,
        "components": {
            "api": "healthy",
            "database": db_status,
            "redis": redis_status
        }
    }), 200 if status == "healthy" else 207

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080)
