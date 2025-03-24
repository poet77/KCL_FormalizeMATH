import pyarrow.parquet as pq
import pandas as pd

# Read the Parquet file
table = pq.read_table('E:/AI4MATH_RESEARCH/Dataset/NuminaMath-CoT/data/train-00004-of-00005.parquet')

# Convert to DataFrame
df = table.to_pandas()

# Convert to JSON format
json_data = df.to_json(orient='records', lines=True)

# Write JSON data to a file
with open('numina05.json', 'w') as f:
    f.write(json_data)