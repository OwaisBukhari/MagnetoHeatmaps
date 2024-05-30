import pandas as pd

# Read the CSV file
csv_file_path = 'yourfile.csv'  # Replace 'input.csv' with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Check if 'ID' column already exists
if 'ID' in df.columns:
    # If 'ID' column already exists, overwrite it
    df['ID'] = range(1, len(df) + 1)
else:
    # If 'ID' column doesn't exist, create a new one
    df.insert(0, 'ID', range(1, len(df) + 1))

# Write the updated data to a new CSV file
output_csv_file_path = 'output.csv'  # Replace 'output.csv' with the desired output file path
df.to_csv(output_csv_file_path, index=False)

print("Auto-incrementing ID column added and written to output.csv")
