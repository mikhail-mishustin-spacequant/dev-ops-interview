# Task 2: Multi-Container Application with Docker Compose

## Objective
Develop a Docker Compose setup for a multi-service application including a web app, database, and cache system.

## Requirements
1. Create a Docker Compose configuration that includes:
   - A web application (use the provided app or create your own)
   - A database service (MySQL or PostgreSQL)
   - A Redis cache service
2. Configure proper networking between services
3. Implement volume management for data persistence
4. Set up appropriate environment variables
5. Configure health checks for all services
6. Ensure the entire stack can be started with a single command

## Starter Files
Basic application files are provided in the `webapp` directory. Your task is to:
1. Review the application code
2. Create a `docker-compose.yml` file in the root of this directory
3. Make any necessary adjustments to the application code to work with your compose configuration
4. Document your solution in a SOLUTION.md file

## Evaluation Criteria
- **Functionality**: Does the multi-container setup work correctly?
- **Configuration**: Is the Docker Compose file properly configured?
- **Dependencies**: Are service dependencies handled correctly?
- **Persistence**: Is data properly persisted using volumes?
- **Documentation**: Is the solution well documented?

## Testing Your Solution
To test your solution:
```bash
# Start the multi-container application
docker-compose up

# Verify all services are running correctly
docker-compose ps

# Test the application functionality
# (Access the web app at http://localhost:8080)
```

## Timeframe
Recommended time: 45-60 minutes
