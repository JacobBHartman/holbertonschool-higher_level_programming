#!/usr/bin/python3
'''
    This module contains a Python script that takes in a string and sends
    a search request to the Star Wars API
'''


if __name__ == '__main__':
    import requests
    from sys import argv

    search = argv[1]
    url = 'https://swapi.co/api/people/' + '?' + 'search={}'.format(search)

    r = requests.get(url)
    r_json = r.json()

    count = r_json['count']
    peeps = r_json['results']
    print("Number of results: {}".format(count))
    for peep in peeps:
        print('{}'.format(peep['name']))
        

