\# IoT Parking Monitoring System - Final Report



\## Team: El manajek

\*Course:\* Internet of Things and Applied Data Science  

\*Professor:\* Dr. Mehmet Ali Akyol  

\*Date:\* December 2025



\## 1. Project Overview

Real-time monitoring of parking space availability using IoT sensors to reduce parking search time by 30% and maintain 95% detection accuracy.



\## 2. Problem Statement

We want to monitor parking space availability for urban parking lots and street-side parking, because it impacts drivers' waiting time, traffic congestion, and city parking management. We will use data from ultrasonic sensors, infrared sensors, and camera-based detection systems at real-time, per-second granularity.



\## 3. Dataset

\- \*Source:\* IoT based Smart Parking System dataset (Kaggle)

\- \*Records:\* 2,769 sensor readings

\- \*Time period:\* January 2020

\- \*Sensors:\* 50 infrared parking sensors

\- \*Columns:\* timestamp, sensor\_id, status (1=occupied, 0=free), raw readings



\## 4. Analysis Results

\- \*Total records:\* 2,769

\- \*Occupied spots:\* 1,396 (50.4%)

\- \*Free spots:\* 1,373 (49.6%)

\- \*Unique sensors:\* 50

\- \*Date range:\* January 1-16, 2020



\## 5. Dashboard Features

\- Real-time parking statistics

\- Interactive sensor filtering

\- Occupancy charts (pie, bar, time series)

\- Raw data display with formatting

\- Responsive web interface



\## 6. Technical Implementation

\- \*Language:\* Python 3.13

\- \*Libraries:\* Pandas, Streamlit, Matplotlib

\- \*Architecture:\* Modular scripts, separate data/analysis/dashboard layers

\- \*Version Control:\* GitHub with team collaboration



\## 7. Challenges \& Solutions

1\. \*Data path issues\* → Fixed with absolute paths and testing scripts

2\. \*File naming inconsistencies\* → Created file verification system

3\. \*Streamlit installation\* → Used python -m streamlit workaround



\## 8. Future Improvements

\- Real-time MQTT data ingestion

\- Machine learning for occupancy prediction

\- Mobile app integration

\- Multi-location dashboard



\## 9. How to Run

```bash

\# Method 1: Using batch file

Double-click START\_HERE.bat



\# Method 2: Manual

cd iot-parking-monitoring-system

python -m streamlit run dashboards/parking\_app.py



\## 10. Team Contributions

\- \*\[Osamah Saleh ]:\* Data analysis, documentation

\- \*\[Loai khalil]:\* Dashboard development, testing  

\- \*\[Tarig Mohammad]:\* Project setup, GitHub management

