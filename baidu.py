import requests
kv = {'wd': 'python'}
r = requests.get('http://www.baidu.com/s', params = kv)
print r.status_code
print r.request.url
print len(r.text)