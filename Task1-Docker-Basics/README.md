# Task 1: Basic Docker Container Deployment

## Objective
Create a Dockerfile for a simple web application that follows best practices for container deployment.

## Requirements
1. Use an appropriate base image (Alpine preferred for size optimization)
2. Create a simple web application using Python Flask or Node.js Express
3. Ensure proper dependency management
4. Configure appropriate port exposure
5. Implement a health check endpoint
6. Optimize the Docker image for size and security
7. Document your solution with clear instructions

## Starter Files
A basic application has been provided in the `app` directory. Your task is to:
1. Review the application code
2. Create a Dockerfile in the root of this directory
3. Document any assumptions or decisions in a SOLUTION.md file

## Evaluation Criteria
- **Functionality**: Does the container run correctly?
- **Best Practices**: Is the Dockerfile following current best practices?
- **Optimization**: Is the resulting image optimized for size?
- **Security**: Are basic security measures implemented?
- **Documentation**: Is the solution well documented?

## Testing Your Solution
To test your solution:
```bash
# Build the Docker image
docker build -t devops-task1 .

# Run the container
docker run -p 8080:8080 devops-task1

# Verify the application by accessing http://localhost:8080
```

## Timeframe
Recommended time: 30-45 minutes
