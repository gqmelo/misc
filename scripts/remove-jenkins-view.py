#!/usr/bin/env python
"""
Creates jenkins views for user
"""
from __future__ import print_function

from getpass import getpass
import argparse
import json
import os
import subprocess
import sys

import requests


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', help='username')
    parser.add_argument('-n', '--name', help='view name (defaults to current branch)')
    args = parser.parse_args(args=args)

    username = args.user
    if not username:
        try:
            username = os.environ['USER']
        except KeyError:
            print("Could not determine current user. Please pass as command line argument")
    password = getpass()
    view_name = args.name
    if not view_name:
        view_name = subprocess.check_output('git rev-parse --abbrev-ref HEAD', shell=True).strip()


    view_url = 'https://eden.esss.com.br/jenkins/user/{username}/my-views/view/{view_name}' \
                        .format(username=username, view_name=view_name)
    delete_url = view_url + '/doDelete'

    r = requests.get(view_url, auth=(username, password))
    if r.status_code not in [requests.codes.ok, requests.codes.created]:
        print("View {} does not exist".format(view_url))
    else:
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        params = {}  # {'name': view_name}
        data = {
            "Submit": "Yes",
            "json": json.dumps({}),
        }
        send_request(delete_url, username, password, data=data, headers=headers)


def send_request(url, user, password, **kwargs):
    print('Sending post to {}'.format(url))
    r = requests.post(url, auth=(user, password), **kwargs)

    if r.status_code not in [requests.codes.ok, requests.codes.created]:
        print('FAILED with code "{}"'.format(r.status_code))
        print(r.text)
    else:
        print('OK')
    print('')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
