# CurlUp-Backend

![Python Version](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.116-blue?logo=fastapi&style=flat)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://pydantic.dev)
![Docker](https://img.shields.io/badge/Docker-v41-blue?logo=docker&style=flat)
![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)


This repository contains the backend codebase for the CurlUp user and vendor management system.


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
docker run -it --name curlup-dev-container -v .:/workspace -p 8000:8000 curlup-dev
```