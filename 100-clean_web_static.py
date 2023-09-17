#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *


env.hosts = ['54.157.129.183', '52.91.125.123']
env.user = "ubuntu"


def do_clean(number=0):
    """ Cleans old versions of web_static """

    number = int(number)

    if number == 0 or number == 1:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
