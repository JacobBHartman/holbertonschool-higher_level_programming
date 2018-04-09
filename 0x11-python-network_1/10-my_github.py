#!/usr/bin/python3
'''
    This module contains a Python script that takes your Github credentials
    and uses the Github API to display your `id`
'''


if __name__ == '__main__':
    import requests
    from sys import argv

    username = argv[1]
    password = argv[2]
    url = "https://api.github.com/user"

    r = requests.get(url, auth=(username, password))
    try:
        print(r.json()['id'])
    except:
        print("None")

