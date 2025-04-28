# Vulnerable Dockerfile with several security issues

# Security Issue #1: Using latest tag instead of specific version
FROM python:latest

# Security Issue #2: Running as root
# No USER directive to change from root

# Security Issue #3: Unnecessary packages installed
RUN apt-get update && \
    apt-get install -y \
    curl \
    vim \
    nmap \  
    netcat \
    telnet \
    sudo

WORKDIR /app

# Security Issue #4: Exposing sensitive information in build
ENV DB_PASSWORD="production_db_password"
ENV API_KEY="prod_api_key_1234567890"

# Copy application files
COPY app/ /app/

# Security Issue #5: Using http instead of https
RUN pip install --no-cache-dir -r requirements.txt -i http://pypi.org/simple

# Security Issue #6: Running with unnecessary capabilities
# No DROP_CAPABILITIES or security_opt settings

# Security Issue #7: Unnecessary port exposure
EXPOSE 22 8080 3306

# Security Issue #8: Running the application as root with debug mode
CMD ["python", "app.py"]
