#!/usr/bin/env python3
# creating a directory with snakebite
from snakebite.client import Client


def createdir(l):
    # function to create a directory
    client = Client('localhost', 9000)

    for path in client.mkdir(l, create_parents=True):
        print(path)
