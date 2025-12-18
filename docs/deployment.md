\# Deployment Documentation



\## Platform

\*Render.com\* (Free Tier)



\## Live URL

https://iot-parking-monitoring-system.onrender.com



\## Deployment Commands

\- \*Build:\* pip install -r requirements.txt

\- \*Start:\* python -m streamlit run dashboards/parking\_app.py --server.port=$PORT --server.address=0.0.0.0



\## Dependencies

\- streamlit==1.51.0

\- pandas==2.2.3

\- matplotlib==3.10.0

\- plotly



\## File Structure for Cloud

\- Main dashboard: dashboards/parking\_app.py

\- Data file: dashboards/SPSIRDATA.csv (copied for cloud)

\- Requirements: requirements.txt in root



\## Notes

\- Free tier sleeps after inactivity (first load: ~30 seconds)

\- Automatic deployment from GitHub on commit

\- Python 3.13.4 environment

