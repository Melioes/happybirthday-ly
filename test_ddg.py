import urllib.request
import urllib.parse
import json
import re

def get_duckduckgo_gif(query, filename):
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query + " gif")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # Find image URLs in duckduckgo
        match = re.search(r'vqd=([\d-]+)', html)
        if not match: return
        vqd = match.group(1)
        
        search_url = f"https://duckduckgo.com/i.js?q={urllib.parse.quote(query + ' gif')}&vqd={vqd}&f=,,,&p=1"
        req2 = urllib.request.Request(search_url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req2).read().decode('utf-8')
        data = json.loads(res)
        
        for result in data['results']:
            if result['image'].endswith('.gif'):
                img_url = result['image']
                print(f"Downloading {img_url} to {filename}")
                req3 = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                with open(filename, 'wb') as f:
                    f.write(urllib.request.urlopen(req3).read())
                return
    except Exception as e:
        print(f"Error {query}: {e}")

get_duckduckgo_gif("minion adorable", "D:/happybirthday/assets/minion.gif")
get_duckduckgo_gif("spongebob cute", "D:/happybirthday/assets/spongebob.gif")
get_duckduckgo_gif("boonie bears", "D:/happybirthday/assets/bear.gif")
