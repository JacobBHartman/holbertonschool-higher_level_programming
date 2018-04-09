#!/usr/bin/python3
'''
    A Python script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in `utf-8`)
'''


if __name__ == '__main__':
    from urllib.request import urlopen, Request
    from sys import argv
    from urllib.error import HTTPError

    url = argv[1]

    try:
        with urlopen(Request(url)) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
