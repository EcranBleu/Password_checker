import hashlib
import sys
import requests

# Grouping arguments in a list
passwords = sys.argv[1:]

# We are creating a loop for each password, in which:
for argument in passwords:

    # We create the hex sha1 hash of the password and store the prefix and suffix in variables
    hashed_pwd = hashlib.sha1(str.encode(argument)).hexdigest()
    hash_prefix, hash_suffix = hashed_pwd[0:5], hashed_pwd[5:].upper()

    # We then form the query to HaveIBeenPwned.com by grouping the API base URL and the first 5 characters of the hash
    url = 'https://api.pwnedpasswords.com/range/' + hash_prefix

    # We create a request object and split the text of that request into a list
    r = requests.get(url)
    suffix_list = r.text.splitlines()

    # We check if the hash is present or not in the answer
    if hash_suffix not in r.text:
        print(f'Password "{argument}" was not leaked! You can use it securely.')
        continue

    for x in suffix_list:
        if x.startswith(hash_suffix):
            occurrences = x.split(':')[-1]
            print(f'Password "{argument}" was leaked {occurrences} times. Do not use it.')