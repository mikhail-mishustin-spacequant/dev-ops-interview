# Task 3: CI/CD Pipeline Implementation

## Objective
Create a CI/CD pipeline configuration for a containerized application using GitHub Actions or GitLab CI.

## Requirements
1. Create a pipeline configuration that:
   - Builds a Docker image for the provided application
   - Runs automated tests
   - Implements semantic versioning
   - Pushes the image to a container registry
   - Deploys to a staging environment
2. Ensure proper secret management
3. Implement branch-based workflow (e.g., different actions for main vs. feature branches)
4. Add basic security scanning

## Starter Files
A basic web application is provided in the `app` directory. Your task is to:
1. Review the application code
2. Create the CI/CD configuration file(s) in the appropriate location
3. Document your solution in a SOLUTION.md file

## Evaluation Criteria
- **Completeness**: Does the pipeline include all required stages?
- **Security**: Are secrets properly managed?
- **Optimization**: Is the pipeline efficient?
- **Best Practices**: Does the configuration follow CI/CD best practices?
- **Documentation**: Is the solution well documented?

## Testing Your Solution
Since the pipeline requires a Git repository and possibly external services, explain in your SOLUTION.md:
- How you would test the pipeline locally (if possible)
- Any mock services or configurations needed for testing
- Expected behavior at each stage of the pipeline

## Timeframe
Recommended time: 60-90 minutes
