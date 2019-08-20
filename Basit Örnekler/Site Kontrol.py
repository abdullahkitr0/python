import requests
print("Abdullahki.tk")
url = input(">> Enter The Web Site Name (exp. 'abdullahki.tk')~# ")
url = ("http://www.%s"%url)
response = requests.get(url)
ok = response.status_code
if ok == 200:
    print(">> Site up")
else:
    print(">> Site is down")
