import requests


r = requests.get('https://api.ipify.org')
ip = r.text
print(ip)
