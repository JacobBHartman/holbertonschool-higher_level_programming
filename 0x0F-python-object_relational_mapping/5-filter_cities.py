#!/usr/bin/python3
""" list all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities \
                 LEFT JOIN states ON cities.state_id = states.id \
                 WHERE states.name=%s \
                 ORDER BY cities.id ASC", (argv[4], ))
    query_rows = cur.fetchall()
    length = len(query_rows)
    for row in range(length - 1):
        print(row[0], end=", ")
    print(row[0])
    cur.close()
    conn.close()
