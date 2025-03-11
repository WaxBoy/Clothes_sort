import pandas as pd
import re

df = pd.read_csv('phone.csv')

for range in df['Usage Range']:
    match = re.search(r'\d+(?:-\d+)')
    if match and '-' in match:
        
print(df['Usage Range'])