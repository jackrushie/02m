import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {response.status_code}, check API again')
    return response


def get_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


def check_pwned_api(password):
    # check password if it exists in API response
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1pass[:5], sha1pass[5:]
    response = request_api_data(first5)
    return get_leaks_count(response, tail)


def main(args):
    for password in args:
        count = check_pwned_api(password)
        if count:
            print(f'Password: {password} was found {count} times')
        else:
            print(f'Password: {password} not found')


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
