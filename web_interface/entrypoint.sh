# #!/bin/sh

echo "JET Restaurant Finder"
echo "Starting app..."
echo ""

exec streamlit run /app/web_interface/main.py \
  --server.address 0.0.0.0 \
  --server.port 8501 \
  --browser.gatherUsageStats false \
  --logger.level=error
