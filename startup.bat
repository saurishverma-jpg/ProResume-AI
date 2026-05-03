@echo off
echo ==========================================
echo   ProResume-AI - Starting...
echo ==========================================

:: Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
call venv\Scripts\activate

:: Install/upgrade dependencies
echo Installing dependencies...
pip install -r requirements.txt --quiet

:: Create feedback directory if not exists
if not exist "feedback" mkdir feedback

:: Start the app
echo.
echo Starting Smart Resume AI...
echo Open browser at: http://localhost:8501
echo.
streamlit run app.py --server.port 8501

pause
