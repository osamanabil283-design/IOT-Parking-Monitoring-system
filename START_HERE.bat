@echo off
cls
color 0A
echo ========================================
echo    🚗 IOT PARKING DASHBOARD
echo ========================================
echo.
echo    Starting your parking dashboard...
echo    Please wait 10-15 seconds...
echo.
echo    When you see "Local URL", open:
echo    http://localhost:8501
echo.
echo    To stop: Press Ctrl+C
echo ========================================
echo.
timeout /t 3 /nobreak > nul

cd /d "C:\Users\Osamah Nabil\Documents\GitHub\iot-parking-monitoring-system"
python -m streamlit run dashboards/parking_app.py