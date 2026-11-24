"""Entry for the make.fun haiku contest "Seventeen Syllables of Debugging".

The poem rests on one concrete scene: the cursor blinking at three a.m.
beside a failing test. The third line turns the story around. The culprit
is not the framework or the machine but the author's own code from last
week.

Running this script writes the haiku to /output/entry.txt.
"""
import os

ENTRY ="""three a.m. cursor
blinks beside the failing test
I wrote this last week"""

os.makedirs('/output', exist_ok=True)
with open('/output/entry.txt', 'w', encoding='utf-8') as f:
    f.write(ENTRY)
