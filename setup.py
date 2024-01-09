from setuptools import setup

setup(
    name='openfortivpn_cookie_extractor',
    version='0.0.1',
    description='Get SVPNCOOKIE from Firefox and start openfortivpn',
    url='https://github.com/MrTomRod/openfortivpn_cookie_extractor',
    author='Thomas Roder',
    packages=['openfortivpn_cookie_extractor'],
    install_requires=[
        'lz4', 'fire'
    ],
    entry_points={
        'console_scripts': [
            'openfortivpn_cookie_extractor=openfortivpn_cookie_extractor.openfortivpn_cookie_extractor:main',
        ],
    },
)
