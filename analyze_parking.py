# PARKING DATA ANALYZER
import pandas as pd

print("=== PARKING DATA ANALYSIS ===")
print()

# Load the CSV file
df = pd.read_csv('data/raw/SPSRDATA.csv')

# Show basic info
print(f"1. Total records in file: {len(df)}")
print()

# Count occupied vs free
occupied = 0
free = 0

for value in df['field2']:
    if value == 1:
        occupied += 1
    elif value == 0:
        free += 1

print(f"2. Parking Status:")
print(f"   - Occupied spots: {occupied}")
print(f"   - Free spots: {free}")
print(f"   - Occupied percentage: {occupied/(occupied+free)*100:.1f}%")
print()

# Count unique sensors
sensors = df['field1'].unique()
print(f"3. Found {len(sensors)} different sensors")
print(f"   First 5 sensors: {sensors[:5]}")
print()

print("=== ANALYSIS COMPLETE ===")