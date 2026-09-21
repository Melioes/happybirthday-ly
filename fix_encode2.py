import re

with open('D:/happybirthday/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<div class=\"pop-word\"[^>]*>.*?</div>', '<div class=\"pop-word\" style=\"font-size: clamp(3rem, 8vw, 5rem); font-weight: bold; color: #f7d070; text-shadow: 0 4px 20px rgba(247, 208, 112, 0.6), 0 0 40px rgba(255,159,67, 0.8);\">岁岁常欢愉</div>', html)
html = re.sub(r'<div class=\"pop-word-author\"[^>]*>.*?</div>', '<div class=\"pop-word-author\" style=\"font-size: 1.2rem; color: rgba(255,255,255,0.8); margin-top: 15px; opacity: 0; transform: translateY(20px);\">—— 你的好友</div>', html)

with open('D:/happybirthday/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
