#!/usr/bin/env python3
# deleting a directory with snakebite
from snakebite.client import Client


def deletedir(l):
    # function to delete a directory
    client = Client('localhost', 9000)

    for path in client.delete(l, recursive=True):
        print(path)
