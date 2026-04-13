FROM python:3.10-slim
# WORKDIR /

# Install the application dependencies
COPY console_app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY models/ models/
COPY console_app/main.py .

CMD ["python", "main.py"]
