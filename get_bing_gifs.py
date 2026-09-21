import urllib.request
import urllib.parse
import re
import os

def download_bing_gif(query, filename):
    url = f"https://cn.bing.com/images/search?q={urllib.parse.quote(query)}&form=HDRSC2&first=1&cw=1177&ch=705"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # Find murl
        matches = re.findall(r'"murl":"([^"]+\.gif)"', html)
        for murl in matches:
            try:
                print(f"Trying {murl} for {query}")
                img_req = urllib.request.Request(murl, headers=headers)
                data = urllib.request.urlopen(img_req, timeout=5).read()
                if len(data) > 10000: # at least 10kb
                    with open(filename, 'wb') as f:
                        f.write(data)
                    print(f"Success: {filename}")
                    return True
            except:
                continue
    except Exception as e:
        print(f"Error: {e}")
    return False

os.makedirs('D:/happybirthday/assets', exist_ok=True)
download_bing_gif('小黄人 gif动图', 'D:/happybirthday/assets/minion.gif')
download_bing_gif('海绵宝宝 派大星 gif动图', 'D:/happybirthday/assets/spongebob.gif')
download_bing_gif('熊二 动画 gif动图', 'D:/happybirthday/assets/bear.gif')
