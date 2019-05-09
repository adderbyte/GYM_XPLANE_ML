from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import os

from setuptools import setup, find_packages

install_requires = [
    'numpy',
    'six',
    'scipy',
    'pillow',
    'pytest',
    'tqdm'
]

setup_requires = [
    'numpy',
    'recommonmark'
]

extras_require = {
    'tf': ['tensorflow>=1.6.0'],
    'gym': ['gym==0.9.5'],
    'tf_gpu': ['tensorflow-gpu>=1.6.0']
}




setup(name='expectedsarsa',
      version='0.1.1',  
      description='expected Sarsa for continuous space',
      url='https://github.com/adderbyte',
      download_url=' ',
      author='adderbyte',
      author_email='adderbyte@icloud.com',
      license='Apache 2.0',
      packages=[package for package in find_packages() if package.startswith('expectedsarsa')],
      install_requires=install_requires,
      setup_requires=setup_requires,
      extras_require=extras_require,
      zip_safe=False)