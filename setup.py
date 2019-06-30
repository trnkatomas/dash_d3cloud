import json
import os
from setuptools import setup

this_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join('dash_d3cloud', 'package.json')) as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    author_email=package["author_email"],
    url=package["url"],
    packages=[package_name],
    package_data={package_name: ['*.json'] + ['*.js']},
    include_package_data=True,
    license=package['license'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[]
)
