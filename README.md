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


 ### Build and Run Container

 > :warning: You need to have Docker Desktop Installed to Develop the CurlUp Backend Locally

- Build
```bash
docker build -t curlup-dev .
```

- Run
```bash
docker run -it --name curlup-dev-container -p 8000:8000 curlup-dev
```
