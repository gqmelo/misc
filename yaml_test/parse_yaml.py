from pprint import pprint

import yaml
import ruamel.yaml

try:
    import xmlrpclib
except ImportError:
    import xmlrpc.client as xmlrpclib

if __name__ == '__main__':
    import os
    with open(os.path.join(os.path.dirname(__file__), 'example.yml'), 'r') as f:
        # print(list(yaml.parse(f)))
        # print(list(yaml.scan(f)))
        print(yaml)
    with open(os.path.join(os.path.dirname(__file__), 'meta.yaml'), 'r') as f:
        data = ruamel.yaml.load(f, ruamel.yaml.RoundTripLoader)
        # data['python'].pop(-2)
        # print data['python']
        # print(ruamel.yaml.dump(data, Dumper=ruamel.yaml.RoundTripDumper))

    client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
    pprint(client.package_releases('conda-build', True))
    pprint(client.release_urls('conda-build', '1.20.1'))
    pprint(client.release_data('conda-build', '1.20.1'))

