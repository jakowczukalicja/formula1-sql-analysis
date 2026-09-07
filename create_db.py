import os
import pandas as pd
import sqlite3

os.makedirs('db', exist_ok=True)

conn = sqlite3.connect('db/formula1.db')

for filename in os.listdir('data'):
    if filename.endswith('.csv'):
        table_name = filename.replace('.csv', '')  
        df = pd.read_csv(f'data/{filename}')
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f'Loaded {filename} as {table_name} successfully')

conn.close()