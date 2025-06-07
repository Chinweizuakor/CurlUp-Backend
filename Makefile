.PHONY: up down build logs shell test lint format migrate upgrade downgrade deploy pull restart shell-prod up-prod down-prod clean clean-prod

# Compose file sets
LOCAL_COMPOSE_FILES := -f docker-compose.yaml -f docker-compose.override.yaml
BUILD_COMPOSE_FILES := -f docker-compose.yaml -f docker-compose.build.yaml
PROD_COMPOSE_FILES := -f docker-compose.prod.yaml
PROD_ENV_FILE := --env-file ./backend/.env.production
LOCAL_ENV_FILE := --env-file ./backend/.env

## Load environment variables from file
#include backend/.env
#export

# Local Dev
up:
	docker-compose $(LOCAL_COMPOSE_FILES) $(LOCAL_ENV_FILE) up

down:
	docker-compose $(LOCAL_COMPOSE_FILES) down

build:
	docker-compose $(LOCAL_COMPOSE_FILES) build

logs:
	docker-compose $(LOCAL_COMPOSE_FILES) logs -f

shell:
	docker-compose $(LOCAL_COMPOSE_FILES) exec fastapi-server /bin/bash

test:
	docker-compose $(LOCAL_COMPOSE_FILES) run --rm fastapi-server pytest

lint:
	docker-compose $(LOCAL_COMPOSE_FILES) run --rm fastapi-server flake8 .

format:
	docker-compose $(LOCAL_COMPOSE_FILES) run --rm fastapi-server black .

migrate:
	docker-compose $(LOCAL_COMPOSE_FILES) run --rm fastapi-server alembic revision -m "create_main_tables"

upgrade:
	docker-compose $(LOCAL_COMPOSE_FILES) run --rm fastapi-server alembic upgrade head

downgrade:
	docker-compose $(LOCAL_COMPOSE_FILES) run --rm fastapi-server alembic downgrade base

# Drop all tables from PostgreSQL
drop-tables:
	docker-compose -f docker-compose.yaml -f docker-compose.override.yaml exec -T postgres_db \
	psql -U postgres -d postgres -f drop_tables.sql

# Cleanup
clean:
	docker system prune -a -f
	npm cache clean --force
	rm -rf .next/
	rm -rf node_modules/
	rm -rf ~/.npm/_cache

# Production

build-for-push:
	docker-compose $(BUILD_COMPOSE_FILES) build

deploy: pull restart upgrade

pull:
	docker-compose $(PROD_COMPOSE_FILES) $(PROD_ENV_FILE) pull --ignore-pull-failures --quiet

restart:
	docker-compose $(PROD_COMPOSE_FILES) $(PROD_ENV_FILE) up -d --no-build

up-prod:
	docker-compose $(PROD_COMPOSE_FILES) $(PROD_ENV_FILE) up

down-prod:
	docker-compose $(PROD_COMPOSE_FILES) $(PROD_ENV_FILE) down

shell-prod:
	@if [ "$$(docker ps -q -f name=fastapi-server)" = "" ]; then \
		echo "Production container not running. Starting up..."; \
		docker-compose $(PROD_COMPOSE_FILES) $(PROD_ENV_FILE) up -d; \
	fi && \
	docker-compose $(PROD_COMPOSE_FILES) exec fastapi-server /bin/bash

# Cleanup
clean-prod:
	docker system prune -a -f
	rm -rf .next/
	rm -rf node_modules/
	rm -rf ~/.npm/_cache

# Drop all tables from PostgreSQL
drop-tables_prod:
	docker-compose -f docker-compose.yaml -f docker-compose.override.yaml exec -T postgres_db \
	psql -U postgres -d postgres -f drop_tables.sql
