import urllib.request
import urllib.parse
import json
import re
import os

def download_baidu_image(keyword, save_path):
    encoded_word = urllib.parse.quote(keyword)
    url = f"https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={encoded_word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word={encoded_word}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://image.baidu.com/'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            urls = re.findall(r'"thumbURL":"(https?://[^"]+)"', html)
            if not urls:
                urls = re.findall(r'"objURL":"(https?://[^"]+)"', html)
            
            for img_url in urls:
                print(f"Found URL for {keyword}: {img_url}")
                try:
                    img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(img_req, timeout=5) as img_res:
                        data = img_res.read()
                        if len(data) > 2000:
                            with open(save_path, 'wb') as f:
                                f.write(data)
                            print(f"Successfully downloaded {keyword} to {save_path} ({len(data)} bytes)")
                            return True
                except:
                    continue
            print(f"Could not download any valid image for {keyword}")
            return False
    except Exception as e:
        print(f"Error scraping {keyword}: {e}")
        return False

os.makedirs('D:/happybirthday/assets', exist_ok=True)
download_baidu_image('\u5c0f\u9ec4\u4eba gif \u53ef\u7231', 'D:/happybirthday/assets/minion.gif')
download_baidu_image('\u6d77\u7ef5\u5b9d\u5b9d gif', 'D:/happybirthday/assets/spongebob.gif')
download_baidu_image('\u718a\u4e8c gif', 'D:/happybirthday/assets/bear.gif')
