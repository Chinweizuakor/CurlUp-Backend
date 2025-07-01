# CurlUp System Backend

![Python Version](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.116-blue?logo=fastapi&style=flat)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://pydantic.dev)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-v16-blue?logo=postgresql&style=flat)
![Nginx](https://img.shields.io/badge/Nginx-v1.28-green?logo=nginx&style=flat)
![Docker](https://img.shields.io/badge/Docker-v41-blue?logo=docker&style=flat)
![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)
[![CurlUp Pipeline CI](https://github.com/Chinweizuakor/CurlUp-Backend/actions/workflows/CI.yaml/badge.svg?branch=main)](https://github.com/Chinweizuakor/CurlUp-Backend/actions/workflows/CI.yaml)

This repository contains the backend codebase for the CurlUp User and Vendor Management System.


## Features
 - Secure Vendor and Customer Management

 - Flexible Appointment Scheduling

 - Payment Integration


 ### Build and Run Container (Server and/or Database)

 > :warning: You need to have Docker Desktop Installed to Develop the CurlUp Backend Locally

- Run Server Only

```bash
# Build the Docker Image
docker build -t curlup-dev .

# Run the Docker Container
docker run -it --name curlup-dev-container -p 8000:8000 curlup-dev
```

- Run Server + Database

```bash
# Start Server and Databasefrom Scratch
docker compose up --build

# Start Server and Database from Existing Images
docker compose up

# Stop Server and Database
docker compose stop

# Stop and Remove Server and Database
docker compose down
```

- Database Operations

```bash
# Connect to the Database Container
docker exec -it curlup-curlup-db-1 bash

# Connect to PostgreSQL
psql -U postgres

\l # List all databases
\l+ # List all databases with more details

\c curlup # Connect to the curlup database
\d # List all tables in the current database
\dt # List all tables in the current database with more details
\dn # List all schemas in the current database

\q # Exit psql
```

- Generate a Secret Key

```bash 
import secrets

# Generate a 256-bit secret key
secret_key = secrets.token_hex(32)
print(secret_key)
# Output: 256-bit secret key
```