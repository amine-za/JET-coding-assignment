JET_ORANGE = \033[38;2;255;128;0m
Turmeric = \033[38;2;246;194;67m
SKY_BLUE = \033[38;2;135;206;235m
RESET = \033[0m

# cli-app:
# 	@echo "Building Docker image..."
# 	@docker build -q -f console_app/Dockerfile -t cli-app . > /dev/null
	
# 	@echo "Starting console app..."
# 	@docker run -it --rm cli-app

# web-app:
# 	@echo "Building Docker image..."
# 	@docker build -q -f web_interface/Dockerfile -t web-app . > /dev/null

# 	@echo "Cleaning up old container that use port 8501 (if any)..."
# 	@docker ps -q --filter "publish=8501" | xargs -r docker stop > /dev/null
# 	@docker ps -aq --filter "publish=8501" | xargs -r docker rm > /dev/null

# 	@echo "Starting web app..."
# 	@docker run -d -p 8501:8501 web-interface:latest > /dev/null

# 	@echo "Opening app in browser..."
# 	@xdg-open http://localhost:8501 > /dev/null

# 	@echo "Web app is running at http://localhost:8501"

.PHONY: help install test run-console run-web docker-build-console docker-build-web docker-run-console docker-run-web clean

help:
	@echo "$(JET_ORANGE)"
	@echo "╔═══════════════════════════════════════════╗"
	@echo "║ JET RESTAURANT FINDER - Makefile Commands ║"
	@echo "╚═══════════════════════════════════════════╝"
	@echo "$(RESET)"
	@echo ""
	@echo "  $(Turmeric)make install              :  $(RESET)Install Python dependencies"
	@echo "  $(Turmeric)make test                 :  $(RESET)Run tests"
	@echo "  $(Turmeric)make run-console          :  $(RESET)Run the console app locally"
	@echo "  $(Turmeric)make run-web              :  $(RESET)Run the Streamlit app locally"
	@echo "  $(Turmeric)make docker-build-console :  $(RESET)Build the console Docker image"
	@echo "  $(Turmeric)make docker-build-web     :  $(RESET)Build the web Docker image"
	@echo "  $(Turmeric)make docker-run-console   :  $(RESET)Run the console app in Docker"
	@echo "  $(Turmeric)make docker-run-web       :  $(RESET)Run the web app in Docker"
	@echo "  $(Turmeric)make clean                :  $(RESET)Remove cache and temporary files"

install:
	pip install -r console_app/requirements.txt
	pip install -r web_interface/requirements.txt

test:
	@PYTHONPATH=. pytest

run-console:
	PYTHONPATH=. python3 console_app/main.py

run-web:
	PYTHONPATH=. streamlit run web_interface/main.py

docker-build-console:
	docker build -f console_app/Dockerfile -t jet-console .

docker-build-web:
	docker build -f web_interface/Dockerfile -t jet-web .

docker-run-console:
	docker run -it --rm jet-console

docker-run-web:
	@docker rm -f jet-web >/dev/null 2>&1 || true
	docker run --name jet-web --rm -p 8501:8501 jet-web
# 	xdg-open http://localhost:8501

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
