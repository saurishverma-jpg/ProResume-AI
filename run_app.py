"""
ProResume-AI - Application Launcher
Run this file to start the application:
    python run_app.py
"""
import subprocess
import sys
import os

def run_app():
    """Launch the Streamlit application"""
    print("🚀 Starting ProResume-AI...")
    print("=" * 50)
    print("Open your browser at: http://localhost:8501")
    print("Press Ctrl+C to stop the application")
    print("=" * 50)

    # Ensure feedback directory exists
    os.makedirs("feedback", exist_ok=True)

    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped.")

if __name__ == "__main__":
    run_app()
