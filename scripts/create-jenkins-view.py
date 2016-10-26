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
            return
    password = getpass()
    view_name = args.name
    if not view_name:
        view_name = subprocess.check_output('git rev-parse --abbrev-ref HEAD', shell=True).strip()

    base_url = 'https://eden.esss.com.br/jenkins/user/{username}/my-views'.format(username=username)
    create_url = base_url + '/createView'
    view_url = base_url + '/view/{view_name}'.format(view_name=view_name)
    config_url = view_url + '/configSubmit'

    r = requests.get(view_url, auth=(username, password))

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    if r.status_code not in [requests.codes.ok, requests.codes.created]:
        params = {}  # {'name': view_name}
        data = {
            "name": view_name,
            "mode": "hudson.model.ListView",
            "Submit": "OK",
            "json": json.dumps(
                {"name": view_name, "mode": "hudson.model.ListView"}
            )
        }
        send_request(create_url, username, password, data=data, headers=headers)

    data = {
        "name": view_name,
        "useincluderegex": "on",
        "includeRegex": ".*-{}-.*".format(view_name),
        "json": json.dumps(
            {
                "name": view_name,
                "columns": [
                        {"stapler-class": "hudson.views.StatusColumn", "$class": "hudson.views.StatusColumn"},
                        {"stapler-class":"hudson.views.WeatherColumn", "$class":"hudson.views.WeatherColumn"},
                        {"stapler-class":"jenkins.plugins.extracolumns.LastBuildConsoleColumn", "$class":"jenkins.plugins.extracolumns.LastBuildConsoleColumn"},
                        {"stapler-class":"hudson.views.BuildButtonColumn", "$class":"hudson.views.BuildButtonColumn"},
                        {"stapler-class":"hudson.views.JobColumn", "$class":"hudson.views.JobColumn"},
                        {"stapler-class":"hudson.views.LastSuccessColumn", "$class":"hudson.views.LastSuccessColumn"},
                        {"stapler-class":"hudson.views.LastFailureColumn", "$class":"hudson.views.LastFailureColumn"},
                        {"stapler-class":"hudson.views.LastDurationColumn", "$class":"hudson.views.LastDurationColumn"},
                ]
            }
        )
    }
    if send_request(config_url, username, password, data=data, headers=headers):
        print("Created view {}".format(view_url))


def send_request(url, user, password, **kwargs):
    print('Sending post to {}'.format(url))
    r = requests.post(url, auth=(user, password), **kwargs)

    if r.status_code not in [requests.codes.ok, requests.codes.created]:
        print('FAILED with code "{}"'.format(r.status_code))
        print(r.text)
        print('')
        return False
    else:
        print('OK')
        print('')
        return True


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
