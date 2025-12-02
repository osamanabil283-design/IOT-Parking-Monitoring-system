import pandas as pd
import os

print("=== PARKING FILE TEST ===")
print()

# Check current folder
print(f"Current folder: {os.getcwd()}")
print()

# Check data/raw folder
if os.path.exists("data"):
    print("✓ 'data' folder exists")
    if os.path.exists("data/raw"):
        print("✓ 'data/raw' folder exists")
        
        # List files in data/raw
        files = os.listdir("data/raw")
        print(f"Files in data/raw: {files}")
        print()
        
        # Try to find the CSV file
        target_file = None
        for file in files:
            if file.lower().endswith('.csv'):
                target_file = file
                print(f"Found CSV file: {file}")
                break
        
        if target_file:
            # Try to load it
            file_path = f"data/raw/{target_file}"
            print(f"Trying to load: {file_path}")
            try:
                df = pd.read_csv(file_path)
                print("✅ SUCCESS! File loaded!")
                print(f"   Rows: {len(df)}")
                print(f"   Columns: {len(df.columns)}")
                print(f"   Column names: {df.columns.tolist()}")
            except Exception as e:
                print(f"❌ ERROR loading file: {e}")
        else:
            print("❌ No CSV files found in data/raw")
    else:
        print("❌ 'data/raw' folder does not exist")
else:
    print("❌ 'data' folder does not exist")