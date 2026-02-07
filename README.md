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

⸻

Author

Created by etenix
(For job application and skill demonstration)