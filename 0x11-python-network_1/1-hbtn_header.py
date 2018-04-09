#!/usr/bin/python3
'''
    this module takes in a URL, sends a request to the URL
    and display the value of the 'X-Request-Id'
'''


if __name__ == '__main__':
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        content = str(response.info())
    for line in content.split('\n'):
        if "X-Request-Id" in line:
            print(line.split(' ')[1])
