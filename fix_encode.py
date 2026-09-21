import re

with open('D:/happybirthday/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the broken text
html = html.replace('곣', '岁岁常欢愉')
html = html.replace(' ĺ', '—— 你的好友')

with open('D:/happybirthday/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
