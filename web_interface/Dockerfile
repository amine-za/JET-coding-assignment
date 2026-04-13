FROM python:3.10-slim

WORKDIR /app

# Install the application dependencies
COPY web_interface/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY web_interface/main.py .
COPY models/ models/
COPY assets/ assets/


COPY web_interface/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]


# CMD ["streamlit", "run", "main.py"]
# CMD ["sh", "-c", "echo 'JET Restaurant Finder'; echo 'Starting app...'; echo ''; exec streamlit run main.py --browser.gatherUsageStats false --logger.level=error 2>/dev/null"]
# CMD ["streamlit", "run", "main.py", "--server.headless=true", "--server.address=0.0.0.0", "--server.port=8501"]
# CMD ["sh", "-c", "streamlit run main.py --server.headless=true --server.address=0.0.0.0 > /dev/null 2>&1"]
# CMD ["sh", "-c", "streamlit run main.py --server.headless=true 2>&1 | grep --line-buffered 'Local URL'"]
# CMD streamlit run main.py --server.headless=true 2>&1 | grep --line-buffered "Local URL" & tail -f /dev/null
# CMD ["sh", "-lc", "streamlit run main.py --server.headless=true --server.address=0.0.0.0 >/dev/null 2>&1 & printf 'Local URL: http://localhost:8501\\n'; wait"]