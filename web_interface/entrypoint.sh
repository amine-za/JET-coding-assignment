#!/bin/sh

echo "JET Restaurant Finder"
echo "Starting app..."
echo ""

streamlit run main.py \
  --browser.gatherUsageStats false \
  --logger.level=error 2>&1 \
  | grep -v "Collecting usage statistics" \
  | grep -v "Network URL:" \
  | grep -v "External URL:"
  # | grep -v "You can now view your Streamlit app in your browser." \

echo "cucu"