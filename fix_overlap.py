import re

with open('D:/happybirthday/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the old draw-text overlay and its JS
html = re.sub(r'<div class=\"draw-text-overlay\".*?</div></div>', '', html)
html = re.sub(r'// 1\. 抖音同款文字发光特效弹出.*?gsap\.to\(drawText, \{ opacity: 0, scale: 1\.5, duration: 1, delay: 2 \}\);', '', html, flags=re.DOTALL)

with open('D:/happybirthday/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
