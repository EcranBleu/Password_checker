import hashlib
import sys
import requests

# Grouping arguments in a list
passwords = sys.argv[1:]

# We are creating a loop for each password, in which:
for argument in passwords:

    # We encode the password and create the hex sha1 hash of that encoded password
    hashed_pwd = hashlib.sha1(str.encode(argument)).hexdigest()

    # We then form the query to HaveIBeenPwned.com by grouping the API base URL and the first 5 characters of the hash
    url = 'https://api.pwnedpasswords.com/range/' + hashed_pwd[0:5]

    # We create a request object, split the text of that request into a list and create the suffix to match in said list
    r = requests.get(url)
    hash_suffixes = r.text.splitlines()
    formatted_suffix = hashed_pwd[5:].upper()

    # We check if the hash is present or not in the answer
    if formatted_suffix not in r.text:
        print(f'Password "{argument}" was not leaked! You can use it securely.')
        continue

    for x in hash_suffixes:
        if x.startswith(formatted_suffix):
            occurrences = x.split(':')[-1]
            print(f'Password "{argument}" was leaked {occurrences} times. Do not use it.')