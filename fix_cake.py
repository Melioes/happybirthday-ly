import re

with open('D:/happybirthday/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix CSS: Add funny font and ensure finale-section is exactly 100vh so cake centers properly
if '<link href="https://fonts.googleapis.com/css2?family=Fredoka+One' not in html:
    html = html.replace('<head>', '<head>\n    <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap" rel="stylesheet">')

html = re.sub(r'\.finale-section\s*\{[^}]*\}', '.finale-section {\n    position: relative; height: 100vh; overflow: hidden; display: flex; flex-direction: column; justify-content: center;\n}', html)

# 2. Fix Button text (less formal)
html = re.sub(r'<button class=\"wish-button.*?id=\"summon-cake-btn\".*?>.*?</button>', '<button class=\"wish-button liquid-glass\" id=\"summon-cake-btn\" style=\"margin-top: 40px;\">🪄 变个魔法蛋糕看看</button>', html)

# 3. Update the 3D Text (English HAPPY BIRTHDAY, deep green, funny font, blessing + name)
blessing_html = '''<div id="cake-blessing" style="position: absolute; top: 15%; left: 0; width: 100%; text-align: center; z-index: 30; pointer-events: none;">
    <div class="pop-word" style="font-family: 'Fredoka One', cursive; font-size: clamp(3rem, 10vw, 6rem); color: #0a5c36; text-shadow: 0 4px 15px rgba(10, 92, 54, 0.4), 0 0 30px rgba(247, 208, 112, 0.8);">HAPPY BIRTHDAY</div>
    <div class="pop-word-author" style="font-size: 1.2rem; color: rgba(255,255,255,0.9); margin-top: 15px; opacity: 0; transform: translateY(20px);">
        愿你每天都能像今天一样开心自在！<br/><br/>—— 梁研
    </div>
</div>'''
html = re.sub(r'<div id=\"cake-blessing\".*?</div>\s*</div>', blessing_html, html, flags=re.DOTALL)

# 4. Fix Cake Position & Add Float/Rotate Animation in JS
# Replace cakeGroup.position.y = -6; with animation logic
if 'cakeGroup.position.y = -6;' in html:
    html = html.replace('cakeGroup.position.y = -6;', 'cakeGroup.position.set(0, -15, 0);\n        gsap.to(cakeGroup.position, { y: -2, duration: 3.5, ease: "back.out(1.2)" });')

with open('D:/happybirthday/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
