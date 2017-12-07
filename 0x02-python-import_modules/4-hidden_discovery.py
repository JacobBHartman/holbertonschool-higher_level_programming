#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dir_len = len(dir(hidden_4))
    for i in range(dir_len):
        if dir(hidden_4)[i][0:2] != "__":
            print("{:s}".format(dir(hidden_4)[i]))
