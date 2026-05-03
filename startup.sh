#!/bin/bash
echo "=========================================="
echo "  ProResume-AI - Starting..."
echo "=========================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install/upgrade dependencies
echo "Installing dependencies..."
pip install -r requirements.txt --quiet

# Create feedback directory if not exists
mkdir -p feedback

# Start the app
echo ""
echo "Starting Smart Resume AI..."
echo "Open browser at: http://localhost:8501"
echo ""
streamlit run app.py --server.port 8501
