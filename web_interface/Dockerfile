FROM python:3.10-slim

WORKDIR /app

ENV PYTHONPATH=/app

# Install the application dependencies
COPY web_interface/requirements.txt web_interface/requirements.txt

RUN pip install --no-cache-dir -r web_interface/requirements.txt

COPY web_interface/main.py web_interface/main.py
COPY models/ models/
COPY assets/ assets/

COPY web_interface/entrypoint.sh web_interface/entrypoint.sh
RUN chmod +x web_interface/entrypoint.sh

EXPOSE 8501

CMD ["streamlit", "run", "web_interface/main.py", "--server.address=0.0.0.0", "--server.port=8501", "--browser.gatherUsageStats=false", "--logger.level=error"]
