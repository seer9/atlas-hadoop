#!/usr/bin/env python3
# retrieves from the HDFS files listed in l and store them
# in the home /tmp folder
from snakebite.client import Client


def download(l):
    # function to download files from HDFS
    client = Client('localhost', 9000)

    for path in client.copyToLocal(l, '/tmp'):
        print(path)
