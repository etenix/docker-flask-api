# Flask REST API with Docker

This is a simple REST API project built with Flask and Docker.
It supports logging and environment variable configuration, and is designed for cloud deployment.

---

## Features

- REST API with Flask
- Docker containerization
- Logging system
- Environment variable support
- Easy deployment

---

## Tech Stack

- Language: Python
- Framework: Flask
- Container: Docker
- OS: Linux

---

## Project Structure

---

## How to Build

Build Docker image:

## How to Run
```bash
docker build -t flask-api .

docker run -p 5000:5000 flask-api

docker run -p 5000:5000 -e APP_NAME=MyAPI flask-api

## API Usage

## POST /hello

## Request:
{
  "name": "Tom"
}
## Response:
{
  "app": "MyAPI",
  "message": "Hello Tom"
}
Purpose

This project was created to practice:
	•	Backend API development
	•	Docker deployment
	•	Basic cloud-ready design
	•	Logging and configuration management

---

## Cloud Deployment (Practice)

This project is designed for deployment on cloud platforms such as:

- AWS EC2
- AWS ECS
- Google Cloud Run
- Azure App Service

Example deployment flow on AWS EC2:

1. Launch EC2 instance (Amazon Linux)
2. Install Docker & Docker Compose
3. Clone this repository
4. Configure environment variables
5. Run with docker-compose

This project was used to practice cloud-based backend deployment.

---

## Future Improvements

- CI/CD with GitHub Actions
- Database integration (PostgreSQL)
- HTTPS support
- Auto scaling

⸻

Author

Created by etenix
(For job application and skill demonstration)