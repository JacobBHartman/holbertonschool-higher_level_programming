#!/usr/bin/python3
'''
    this module contains a scrpt that fetches a particular URL
'''

if __name__ == '__main__':
    import urllib.request
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
