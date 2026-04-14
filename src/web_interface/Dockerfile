FROM python:3.10-slim

WORKDIR /app

# Ensures Python can resolve local modules (/src/models)
ENV PYTHONPATH=/app/src

# Copy requirements file for dependency installation
COPY src/web_interface/requirements.txt src/web_interface/requirements.txt

# Install dependencies without storing pip cache (keeps image smaller and avoids reuse of downloaded packages)
RUN pip install --no-cache-dir -r src/web_interface/requirements.txt

COPY src/web_interface/main.py src/web_interface/main.py
COPY src/models/ src/models/
COPY src/web_interface/assets/ src/web_interface/assets/

EXPOSE 8501

# Run Streamlit web app, expose it on all network interfaces for Docker access, disable usage tracking, and set logging to debug level
CMD ["streamlit", "run", "src/web_interface/main.py", "--server.address=0.0.0.0", "--server.port=8501", "--browser.gatherUsageStats=false", "--logger.level=debug"]
