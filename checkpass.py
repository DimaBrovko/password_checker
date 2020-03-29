import requests
import hashlib

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/ra`nge/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check')
    return res
def pwned_api_check(password):
    #check password if it exist in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password
request_api_data('123')