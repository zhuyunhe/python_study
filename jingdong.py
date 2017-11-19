import requests
url = 'https://item.jd.com/1502515.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:2000])
except:
    print("fail")