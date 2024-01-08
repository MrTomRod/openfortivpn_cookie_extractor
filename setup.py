from setuptools import setup, find_packages

setup(
    name='openfortivpn_cookie_extractor',
    version='0.0.1',
    description='Get SVPNCOOKIE from Firefox and start openfortivpn',
    url='https://github.com/MrTomRod/openfortivpn_cookie_extractor',
    author='Thomas Roder',
    packages=find_packages(),
    install_requires=[
        'lz4', 'fire'
    ],
    entry_points={
        'console_scripts': [
            'vpn=openfortivpn_cookie_extractor.openfortivpn_cookie_extractor:main',
        ],
    },
)
