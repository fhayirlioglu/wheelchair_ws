#!/usr/bin/env python3
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()
d['packages'] = ['srl_tracking_logfile_import']
d['package_dir'] = {'':'src'}

setup(**d)