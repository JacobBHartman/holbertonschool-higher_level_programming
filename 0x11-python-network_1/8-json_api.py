#!/usr/bin/python3
'''
    A Python script that takes in a letter and sends a POST
    request to a particular url with th eletter as a parameter
'''


if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) <= 1:
        q = ""
    else:
        q = argv[1]
    values = {'q': q}

    r = requests.post(url, values)
    try:
        data = r.json()
        if data is None:
            print("No Result")
        else:
            print("[{}] {}".format(data['id'], data['name']))
    except ValueError as error:
        print("Not a valid JSON")
