from setuptools import setup

setup(
    name='scrapegoat',
    version='0.1.0',
    packages=['scrapegoat', 'scrapegoat.engine'],
    url='https://github.com/faysal-ishtiaq/scrapegoat',
    license='GNU General Public License v3.0',
    author='faysal',
    author_email='f.i.rabby@gmail.com',
    description='A simple data miner.',
    entry_points='''
            [console_scripts]
            scrapegoat=scrapegoat.main:cli
        ''',
)
