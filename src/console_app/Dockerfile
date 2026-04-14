FROM python:3.10-slim

WORKDIR /app

# Install the application dependencies
COPY src/console_app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code and shared models
COPY src/models/ models/
COPY src/console_app/main.py .

# Run the console application
CMD ["python", "main.py"]
