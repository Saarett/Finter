from setuptools import setup


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='finter',
    version='0.0.1',
    packages=[''],
    url='https://github.com/Saarett/Finter',
    author='settinger',
    author_email='saarettinger@gmail.com',
    description='Read, parse and output financial files into a single report',
    long_description=readme,
    license=license
)
