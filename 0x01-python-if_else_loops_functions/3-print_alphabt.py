#!/usr/bin/python3

for i in range(ord('a'), ord('z') + 2):
    if i != ord('q') and i != ord('e'):
        print("{:c}".format(i), end="")
