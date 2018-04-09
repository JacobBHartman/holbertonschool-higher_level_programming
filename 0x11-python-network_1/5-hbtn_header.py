#!/usr/bin/python3
'''
    This module contains a Python script that takes in a URL, sends
    a request to the URL and displays the value of a particular
    variable
'''

if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    variable = 'X-Request-Id'
    content = requests.get(url)

    print("{}".format(content.headers[variable]))
