import urllib.request
import json

def download(url, filename):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            with open(filename, 'wb') as f:
                f.write(response.read())
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed {filename}: {e}")

# We will use Baidu Image Search API or standard proxy to get GIFs
urls = [
    ("https://gips2.baidu.com/it/u=309328476,3366889416&fm=3028&app=3028&f=GIF&fmt=auto&q=100&size=f600_800", "D:/happybirthday/assets/minion.gif"),
    ("https://gips3.baidu.com/it/u=2362483569,2166669931&fm=3028&app=3028&f=GIF&fmt=auto&q=100&size=f600_800", "D:/happybirthday/assets/spongebob.gif"),
    ("https://gips0.baidu.com/it/u=3563919639,1147571343&fm=3028&app=3028&f=GIF&fmt=auto&q=100&size=f600_800", "D:/happybirthday/assets/bear.gif")
]

for url, path in urls:
    download(url, path)
