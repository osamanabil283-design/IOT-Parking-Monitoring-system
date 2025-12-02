import pandas as pd

print("🚗 IOT PARKING SYSTEM - FIRST SUCCESSFUL ANALYSIS 🚗")
print("=" * 50)

# Load the CORRECT file
df = pd.read_csv('data/raw/SPSIRDATA.csv')

print(f"📊 Dataset Statistics:")
print(f"   Total records: {len(df):,}")
print(f"   Total columns: {len(df.columns)}")
print()

# Parking occupancy
occupied = (df['field2'] == 1).sum()
free = (df['field2'] == 0).sum()
total = occupied + free

print(f"🚗 Parking Occupancy:")
print(f"   Occupied spots: {occupied:,} ({occupied/total*100:.1f}%)")
print(f"   Free spots: {free:,} ({free/total*100:.1f}%)")
print()

# Sensors
sensors = df['field1'].nunique()
print(f"🔧 Sensor Information:")
print(f"   Unique sensors: {sensors}")
print(f"   Sample sensors: {df['field1'].unique()[:5]}")
print()

# Save results
results = f"""PARKING ANALYSIS RESULTS
=========================
Analysis Date: {pd.Timestamp.now()}
Total Records: {len(df):,}
Occupied Spots: {occupied:,} ({occupied/total*100:.1f}%)
Free Spots: {free:,} ({free/total*100:.1f}%)
Unique Sensors: {sensors}
First Sensor Reading: {df['created_at'].iloc[0]}
Last Sensor Reading: {df['created_at'].iloc[-1]}
"""

with open('data/processed/analysis_results.txt', 'w') as f:
    f.write(results)

print("✅ Analysis complete!")
print("📁 Results saved to: data/processed/analysis_results.txt")