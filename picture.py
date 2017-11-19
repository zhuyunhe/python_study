import requests
import os

url = "https://img14.360buyimg.com/n0/jfs/t1132/251/682240386/86416/a7d87ef5/553da24cN6261521f.jpg"
root = '/Users/zyh/Downloads/'
path = root + url.split('/')[-1]
print path

try:
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print 'success'
    else:
        print 'fail'
except expression as identifier:
    print 'fail'