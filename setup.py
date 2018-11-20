
from setuptools import setup, find_packages
from proto.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='proto',
    version=VERSION,
    description='Making managing home servers easier!',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='ProtoServer',
    author_email='protoserverio@gmail.com',
    url='https://github.com/protoserver/proto-cli',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'proto': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        proto = proto.main:main
    """,
)
