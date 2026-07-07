import os
import pandas as pd

# Use script directory to locate the folder dynamically
script_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(script_dir, "All datasets")

if not os.path.exists(folder_path):
    # Fallback to local subdirectory if not found
    folder_path = "All datasets"

os.chdir(folder_path)
print("Current working directory:", os.getcwd())

# Listed all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Initialized an empty list to store individual DataFrames
dataframes = []

# Loop through and read each CSV file
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    try:
        df = pd.read_csv(file_path)
        dataframes.append(df)
        print(f"Loaded: {file}")
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Merge all DataFrames into a single one
merged_df = pd.concat(dataframes, ignore_index=True)

# Save to a new CSV using an absolute path
output_path = os.path.join(folder_path, "combined_jmp_wash_dataset.csv")
try:
    merged_df.to_csv(output_path, index=False)
    print(f"\nMerged {len(dataframes)} datasets. Output saved as: {output_path}")
except PermissionError as e:
    print(f"PermissionError: {e}\nIs the file open in another program?")
