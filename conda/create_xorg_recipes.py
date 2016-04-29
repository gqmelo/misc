from __future__ import unicode_literals
import subprocess
import re
import os


META_YAML = '''package:
  name: {name}
  version: {version}

source:
  fn: {filename}
  url: {url}

build:
  number: 0

about:
  home: http://www.x.org/archive/X11R7.7
  license: MIT License
'''

BUILD_SH = '''#!/bin/bash

export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:$PREFIX/share/pkgconfig
./configure --prefix=$PREFIX
make -j${CPU_COUNT}
make install
'''

HTTP_URL = 'http://xorg.mirrors.pair.com/X11R7.7/src/lib/'

filenames = subprocess.check_output(['curl', '-l', 'ftp://mirror.csclub.uwaterloo.ca/x.org/X11R7.7/src/lib/'])
filenames = filenames.splitlines()
filenames = [f for f in filenames if f.endswith('.tar.bz2')]

for filename in filenames:
    m = re.match('(.+?)-(.+?)\.tar\.bz2', filename)
    if not m:
        print 'filename "{}" do not match'.format(filename)
        continue

    template = {}

    template['name'] = name = m.group(1).lower()
    template['version'] = version = m.group(2)
    template['url'] = url = HTTP_URL + filename
    template['filename'] = filename

    if os.path.exists(name):
        print '{} name already exists, skipping'.format(name)
        continue

    os.mkdir(name)

    build_sh_filename = os.path.join(name, 'build.sh')
    with open(build_sh_filename, 'w') as f:
        f.write(BUILD_SH)
    os.system('chmod 755 {}'.format(build_sh_filename))


    meta_yaml_filename = os.path.join(name, 'meta.yaml')
    with open(meta_yaml_filename, 'w') as f:
        f.write(META_YAML.format(**template))
    os.system('chmod 644 {}'.format(build_sh_filename))


