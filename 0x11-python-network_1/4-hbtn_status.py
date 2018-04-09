#!/usr/bin/python3
'''
    This module contains a Python script that fetches a particular URL
'''

if __name__ == '__main__':
    import requests
    url = 'https://intranet.hbtn.io/status'
    content = requests.get(url).text
    
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
