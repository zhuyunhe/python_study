
import requests
url = 'https://www.amazon.cn/%E5%AF%92%E5%A4%9C-%E5%B7%B4%E9%87%91/dp/B009PG5XQQ/ref=sr_1_1?ie=UTF8&qid=1510672506&sr=8-1&keywords=%E5%AF%92%E5%A4%9C'
kv = {'user-agent': 'Mozilla/5.0'}
try:
    r = requests.get(url, headers = kv)
    print r.status_code
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:2000])
except:
    print("fail")