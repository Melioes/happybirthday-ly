import urllib.request
import urllib.parse
import json
import re

def download_img(keyword, save_path):
    encoded_word = urllib.parse.quote(keyword)
    url = f"https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&queryWord={encoded_word}&word={encoded_word}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            urls = re.findall(r'"thumbURL":"(https?://[^"]+)"', html)
            for img_url in urls:
                try:
                    img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(img_req, timeout=5) as img_res:
                        data = img_res.read()
                        if len(data) > 5000: # at least 5kb
                            with open(save_path, 'wb') as f:
                                f.write(data)
                            print(f"Downloaded {save_path}")
                            return True
                except:
                    continue
    except:
        pass

download_img('\u5c0f\u9ec4\u4eba\u52a8\u56fe', 'D:/happybirthday/assets/minion.gif')
download_img('\u6d77\u7ef5\u5b9d\u5b9d\u52a8\u56fe', 'D:/happybirthday/assets/spongebob.gif')
