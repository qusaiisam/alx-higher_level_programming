#!/usr/bin/python3

for j1 in range(0, 10):
    for j2 in range(j1 + 1, 10):
        if j1 == 8 and j2 == 9:
            print("{}{}".format(j1, j2))
        else:
            print("{}{}".format(j1, j2), end=", ")
