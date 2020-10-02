from setuptools import setup

def get_requires():
    path = 'nalog_scarapper/requirements.txt'
    filepath = pkg_resources.resource_filename(__name__, path)
    with open(filepath) as file:
        packages = [name.rstrip() for name in file.readlines()]
    return packages

setup(
    name='RASFS scrapper',
    version='',
    packages=['nalog_scrapper'],
    url='https://github.com/ponomarevkonst/financial-statement-scrapper',
    license='MIT',
    author='Konstantin Ponomarev',
    author_email='ponomarevkonst@gmail.com',
    description='Selenium based web scrapper for retrieving financial statements indexes.',
    install_requires=get_requires()
)
