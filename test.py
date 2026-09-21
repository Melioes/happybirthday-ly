import urllib.request
import base64
import json

def fetch_b64(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            return base64.b64encode(response.read()).decode('utf-8')
    except Exception as e:
        return str(e)

# Cute Minion
minion = fetch_b64('https://s3.bmp.ovh/imgs/2021/09/a3c2cf5ebba61a9c.jpg') 
print('Done')
