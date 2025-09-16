FROM python:3.9-slim

WORKDIR /sf_automation

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 3000

HEALTHCHECK CMD curl --fail http://localhost:80/_stcore/health

#ENTRYPOINT ["streamlit", "run", "snowchain.py", "--server.port=80", "--server.address=0.0.0.0"]
ENTRYPOINT ["python3", "slack_interface.py"]