#!/usr/bin/python3
'''
    This Python script takes in a URL and an eamil, sends a POST
    request to the passed URL with the email as a parameter, and
    displays the body of the response
'''


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    email = argv[2]

    values = {'email': email}
    r = requests.post(url, data=values)
    print("{}".format(r.text))
