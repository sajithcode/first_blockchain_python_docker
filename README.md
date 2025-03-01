# Simple Blockchain in Python with Docker

## Introduction
This project implements a simple blockchain using Python and runs it inside a Docker container. The blockchain consists of basic block validation and proof-of-work mechanisms.

## Project Structure
```
📂 simple-blockchain
├── 📄 main.py              # Main blockchain 
├── 📄 Block.py              # blockchain class 
├── 📄 Dockerfile          # Docker configuration 
├── 📄 requirements.txt    # Python dependencies
└── 📄 README.md           # Project documentation
```

## Prerequisites
Ensure you have the following installed:
- [Docker](https://www.docker.com/get-started)

## Getting Started

### 1. Clone the Repository
```sh
git clone https://github.com/your-repo/simple-blockchain.git
cd simple-blockchain
```

### 2. Build the Docker Image
```sh
docker build -t simple-blockchain .
```

### 3. Run the Docker Container
```sh
docker run --rm simple-blockchain
```

If the application runs a web server (e.g., Flask), expose a port:
```sh
docker run -p 5000:5000 simple-blockchain
```

## Updating the Application
If you modify `app.py`, rebuild and restart the container:
```sh
docker build -t simple-blockchain .
docker run --rm simple-blockchain
```

## (Optional) Run with Docker Compose
If using `docker-compose.yml`:
```sh
docker-compose up --build
```

## License
This project is licensed under the MIT License.

