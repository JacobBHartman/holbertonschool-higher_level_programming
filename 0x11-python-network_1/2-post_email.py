#!/usr/bin/python3
'''
    This Python script takes in a URL and an eamil, sends a POST
    request to the passed URL with the email as a parameter, and
    displays the body of the response (decoded in `utf-8`)
'''


if __name__ == '__main__':
    from urllib import request, parse
    from sys import argv
    
    url = argv[1]
    email = argv[2]

    values = {'email': email}
    
    data = parse.urlencode(values)
    data = data.encode('ascii')

    req = request.Request(url, data)
    with request.urlopen(req) as response:
        content = response.read()
    print(content.decode('utf-8'))
