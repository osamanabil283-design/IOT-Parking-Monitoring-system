import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="IoT Parking Monitor",
    page_icon="🚗",
    layout="wide"
)

# Title
st.title("🚗 IoT Smart Parking Monitoring System")
st.markdown("*Team:* El manajek | *Course:* IoT and Applied Data Science - Fall 2025")

# Load data
@st.cache_data
def load_data():
    import os
    
    # Try multiple paths for different environments
    if os.path.exists('data/raw/SPSIRDATA.csv'):
        # Local development path
        df = pd.read_csv('data/raw/SPSIRDATA.csv')
    elif os.path.exists('SPSIRDATA.csv'):
        # Root folder path (alternative local)
        df = pd.read_csv('SPSIRDATA.csv')
    elif os.path.exists('dashboards/SPSIRDATA.csv'):
        # Render.com deployment path
        df = pd.read_csv('dashboards/SPSIRDATA.csv')
    else:
        # If no file found, create empty dataframe with error message
        st.error("❌ CSV data file not found! Please check file locations.")
        # Create empty dataframe to prevent crashes
        df = pd.DataFrame(columns=['created_at', 'entry_id', 'field1', 'field2', 'field3'])
    
    # Convert timestamp if we have data
    if not df.empty:
        df['created_at'] = pd.to_datetime(df['created_at'])
    
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔧 Filters")
selected_sensors = st.sidebar.multiselect(
    "Select Sensors:",
    options=df['field1'].unique(),
    default=df['field1'].unique()[:5]
)

date_range = st.sidebar.date_input(
    "Date Range:",
    value=[df['created_at'].min().date(), df['created_at'].max().date()]
)

# Filter data
filtered_df = df[
    (df['field1'].isin(selected_sensors)) &
    (df['created_at'].dt.date >= date_range[0]) &
    (df['created_at'].dt.date <= date_range[1])
]

# Metrics in columns
st.subheader("📊 Real-Time Parking Status")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Records", f"{len(filtered_df):,}")

with col2:
    occupied = (filtered_df['field2'] == 1).sum()
    st.metric("Occupied Spots", occupied)

with col3:
    free = (filtered_df['field2'] == 0).sum()
    st.metric("Free Spots", free)

with col4:
    occupancy_rate = occupied / len(filtered_df) * 100 if len(filtered_df) > 0 else 0
    st.metric("Occupancy Rate", f"{occupancy_rate:.1f}%")

# Visualizations
st.subheader("📈 Parking Analytics")

# Create two columns for charts
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    # Pie chart
    st.write("*Parking Occupancy Distribution*")
    fig1, ax1 = plt.subplots(figsize=(6, 6))
    ax1.pie([occupied, free], 
            labels=['Occupied', 'Free'], 
            autopct='%1.1f%%',
            colors=['#FF6B6B', '#4ECDC4'])
    ax1.axis('equal')
    st.pyplot(fig1)

with chart_col2:
    # Bar chart by sensor
    st.write("*Occupancy by Sensor*")
    sensor_counts = filtered_df.groupby('field1')['field2'].mean().sort_values(ascending=False)
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sensor_counts.head(10).plot(kind='bar', ax=ax2, color='#45B7D1')
    ax2.set_xlabel("Sensor ID")
    ax2.set_ylabel("Occupancy Rate")
    ax2.set_title("Top 10 Sensors by Occupancy")
    plt.xticks(rotation=45)
    st.pyplot(fig2)

# Time series chart
st.subheader("📅 Occupancy Over Time")
time_agg = st.selectbox("Aggregation:", ["Hour", "Day", "Month"], index=1)

if time_agg == "Hour":
    filtered_df['time_group'] = filtered_df['created_at'].dt.floor('H')
elif time_agg == "Day":
    filtered_df['time_group'] = filtered_df['created_at'].dt.date
else:
    filtered_df['time_group'] = filtered_df['created_at'].dt.to_period('M').astype(str)

time_series = filtered_df.groupby('time_group')['field2'].mean().reset_index()
time_series.columns = ['Time', 'Occupancy_Rate']

fig3, ax3 = plt.subplots(figsize=(12, 4))
ax3.plot(time_series['Time'], time_series['Occupancy_Rate'] * 100, marker='o', linewidth=2)
ax3.set_xlabel("Time")
ax3.set_ylabel("Occupancy Rate (%)")
ax3.set_title(f"Parking Occupancy Over Time ({time_agg}ly)")
ax3.grid(True, alpha=0.3)
plt.xticks(rotation=45)
st.pyplot(fig3)

# Data table
st.subheader("📋 Raw Sensor Data")
st.dataframe(
    filtered_df.head(100),
    column_config={
        "created_at": "Timestamp",
        "entry_id": "Entry ID",
        "field1": "Sensor ID",
        "field2": st.column_config.NumberColumn(
            "Status",
            help="1 = Occupied, 0 = Free",
            format="%d"
        ),
        "field3": "Raw Reading"
    },
    hide_index=True,
    use_container_width=True
)

# Footer
st.markdown("---")
st.markdown("*IoT Parking Monitoring System* | Data Source: IoT Smart Parking Dataset | Last Updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))