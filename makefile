cli-app:
	@echo "Building Docker image..."
	@docker build -q -f console_app/Dockerfile -t cli-app . > /dev/null
	
	@echo "Starting console app..."
	@docker run -it --rm cli-app

web-app:
	@echo "Building Docker image..."
	@docker build -q -f web_interface/Dockerfile -t web-app . > /dev/null

	@echo "Cleaning up old container that use port 8501 (if any)..."
	@docker ps -q --filter "publish=8501" | xargs -r docker stop > /dev/null
	@docker ps -aq --filter "publish=8501" | xargs -r docker rm > /dev/null

	@echo "Starting web app..."
	@docker run -d -p 8501:8501 web-interface:latest > /dev/null

	@echo "Opening app in browser..."
	@xdg-open http://localhost:8501 > /dev/null

	@echo "Web app is running at http://localhost:8501"

# clean:
# 	@echo "Stopping web-app and cli-app containers..."
# 	@docker stop web-app >/dev/null
# 	@docker stop cli-app >/dev/null
	
# 	@echo "Removing web-app and cli-app containers..."
# 	@docker rm -f web-app 2>/dev/null || true
# 	@docker rm -f web-app >/dev/null
# 	@docker rm -f cli-app >/dev/null
	
# 	@echo "Stopped and removed."

.PHONY: cli-app web-app