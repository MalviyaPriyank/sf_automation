# =============================
# ===== FRONTEND BUILD ========
# =============================
FROM node:20 AS frontend-build
WORKDIR /app/frontend
COPY frontend/package*.json ./
COPY frontend ./
RUN npm install && npm run build


# =============================
# ===== BACKEND BUILD =========
# =============================
FROM python:3.11-slim-bookworm AS backend-build
WORKDIR /app
COPY . .
# System dependencies for MSSQL
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    gnupg \
    unixodbc \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Microsoft SQL Server ODBC driver
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc \
    | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg && \
    echo "deb [arch=amd64,arm64,armhf signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" \
    > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    rm -rf /var/lib/apt/lists/*

# Copy backend requirements
COPY requirements.txt .

# Install backend dependencies in *build* stage
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/server.py .


# =============================
# ===== FINAL IMAGE ===========
# =============================
FROM debian:stable-slim

WORKDIR /app
COPY . .

# Python + nginx + ODBC
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    nginx \
    unixodbc \
    build-essential \
    curl \
    git \
    gnupg \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*
#    && apt-get clean

# Copy backend code
# COPY --from=backend-build /app /app

# Microsoft SQL Server ODBC driver
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc \
    | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg && \
    echo "deb [arch=amd64,arm64,armhf signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" \
    > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    rm -rf /var/lib/apt/lists/*

# Create venv for Python packages (PEP 668 safe)
RUN python3 -m venv /app/venv
ENV BACKEND_CORS_ORIGIN='http://0.0.0.0:5173'
# ENV OAUTH_REDIRECT_URI='http://localhost:80/api/auth/callback'
ENV OAUTH_REDIRECT_URI='https://frosty.thegyrus.com/api/auth/callback'
# ENV FRONTEND_URL='http://localhost:80'
ENV FRONTEND_URL='https://frosty.thegyrus.com/'
ENV MONGO_URI='mongodb+srv://samuel:x8xKpSX9v2EgewBH@mongodb-cluster.yv1iz2o.mongodb.net/?appName=mongodb-cluster'
ENV CLIENT_ID='662907179065-d8fogs9f5m468nktki41pgg5qtt06kb6.apps.googleusercontent.com'
ENV CLIENT_SECRET='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'
ENV PATH="/app/venv/bin:$PATH"
# Ensure Python can import backend package
ENV PYTHONPATH="/app:/app/backend"

# Install requirements inside the venv
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy frontend build
COPY --from=frontend-build /app/frontend/dist /app/frontend

# Copy nginx config
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 4004

# Run FastAPI app behind nginx
CMD /app/venv/bin/uvicorn main:app --host 0.0.0.0 --port 4004 --app-dir /app/backend & nginx -g "daemon off;"
