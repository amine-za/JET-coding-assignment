JET_ORANGE = \033[38;2;255;128;0m
Turmeric = \033[38;2;246;194;67m
SKY_BLUE = \033[38;2;135;206;235m
RESET = \033[0m

PORT ?= 8501
BASE_PYTHON ?= python3
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip


.PHONY: help install test run-console run-web docker-build-console docker-build-web docker-run-console docker-run-web docker-stop-web docker-logs-web clean

help:
	@echo "$(JET_ORANGE)"
	@echo "╔═══════════════════════════════════════════╗"
	@echo "║ JET RESTAURANT FINDER - Makefile Commands ║"
	@echo "╚═══════════════════════════════════════════╝$(RESET)"
	@echo "  $(Turmeric)make install              :  $(RESET)Install Python dependencies"
	@echo "  $(Turmeric)make test                 :  $(RESET)Run tests"
	@echo "  $(Turmeric)make run-console          :  $(RESET)Run the console app locally"
	@echo "  $(Turmeric)make run-web              :  $(RESET)Run the Streamlit app locally"
	@echo "  $(Turmeric)make docker-build-console :  $(RESET)Build the console Docker image"
	@echo "  $(Turmeric)make docker-build-web     :  $(RESET)Build the web Docker image"
	@echo "  $(Turmeric)make docker-run-console   :  $(RESET)Run the console app in Docker"
	@echo "  $(Turmeric)make docker-run-web       :  $(RESET)Run the web app in Docker"
	@echo "  $(Turmeric)make docker-stop-web      :  $(RESET)Stop the running web container"
	@echo "  $(Turmeric)make docker-logs-web      :  $(RESET)View logs of the web container"
	@echo "  $(Turmeric)make clean                :  $(RESET)Remove cache and temporary files"


#  Creates a local Python environment used for all development commands.
#  This ensures reproducibility across machines.
venv:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Creating virtual environment, may take few secs..."; \
		$(BASE_PYTHON) -m venv $(VENV); \
		echo "Virtual environment created successfully"; \
	fi


# Installs both console and web application requirements into the venv.
# Must be executed before running any application or tests.
install: venv
	@echo "Installing application dependencies..."
	@$(PIP) install -r src/console_app/requirements.txt > /dev/null
	@$(PIP) install -r src/web_interface/requirements.txt > /dev/null
	@echo "Dependencies installed successfully"

test: install
	@PYTHONPATH=src $(PYTHON) -m pytest

run-console: install
	@PYTHONPATH=src $(PYTHON) src/console_app/main.py

run-web: install
	@echo "Starting Streamlit app on http://localhost:$(PORT)..."
	@PYTHONPATH=src $(PYTHON) -m streamlit run src/web_interface/main.py

docker-build-console:
	@echo "Building console application Docker image..."
	@docker build -f src/console_app/Dockerfile -t jet-console . 
	@echo "Console application Docker image built successfully."

docker-build-web:
	@echo "Building web interface Docker image..."
	@docker build -f src/web_interface/Dockerfile -t jet-web . 
	@echo "Web interface Docker image built successfully."


# Builds and runs containerized versions of the console.
# Used for environment parity across development and production.
docker-run-console: docker-build-console
	@echo "Starting console application..."
	@docker run -it --rm jet-console

# Builds and runs the web app in Docker:
# 1- Stops + removes existing container if it exists, and prevents Make from failing with 'true'
# 2- Running the container with detached mode (background) with fixed containers name for easy management, and with port mapping 
# 3- Opens the app in the default browser (Linux/macOS) or prints the URL if not supported
docker-run-web: docker-build-web
	@echo "Starting web interface on http://localhost:$(PORT)..."
	@docker rm -f jet-web >/dev/null 2>&1 || true
	@docker run -d --name jet-web -p $(PORT):8501 jet-web
	@xdg-open http://localhost:$(PORT) 2>/dev/null || open http://localhost:$(PORT) 2>/dev/null || echo "Open http://localhost:$(PORT) manually"

docker-stop-web:
	@docker rm -f jet-web >/dev/null 2>&1 || true

docker-logs-web:
	@docker logs -f jet-web

clean:
	@echo "Cleaning up cache and temporary files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@echo "Done."
