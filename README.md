# AI IT Support System

This project implements an AI-driven IT support agent capable of automating common IT tasks such as password resets and software installations using **Flask**, **NLP**, **RAG**, and **AI-based reasoning**.

### Features:
- Automated IT support for Tier-1 tasks
- Natural Language Processing for understanding user queries
- Retrieval-Augmented Generation (RAG) for knowledge-based answers
- Scalable cloud deployment with Docker

### Requirements:
- Python 3.x
- Docker (for containerization)
- Flask (for API)

### How to Run:
1. Clone the repository
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the app:
    ```
    python app.py
    ```

### Deployment:
1. Build Docker image:
    ```
    docker build -t ai-it-support .
    ```
2. Push the image to your preferred cloud platform for deployment.
