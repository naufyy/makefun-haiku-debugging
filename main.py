import os

ENTRY = """three a.m. cursor
blinks beside the failing test
I wrote this last week"""

os.makedirs('/output', exist_ok=True)
with open('/output/entry.txt', 'w', encoding='utf-8') as f:
    f.write(ENTRY)
