import pandas as pd
import gzip

file = '../raw data/users_items.json.gz'

with gzip.open(file, 'rb') as f:
    json_content = f.read().decode('utf-8')

df = pd.read_json(json_content)

print(df)