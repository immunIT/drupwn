from setuptools import setup, find_packages

setup(
    author='ImmunIT',
    author_email='rd@immunit.ch',

    name='drupwn',
    version='1.0.3',
    licence='GPLv3',

    url='https://github.com/immunIT/drupwn',

    description='Drupal enumeration & exploitation tool',
    long_description='Drupwn claims to provide an efficient way to gather drupal information. Further information on our github project.',
    long_description_content_type='text/plain',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],

    keywords="pentesting exploit enumeration drupal",

    projects_urls={
        'Documentation': 'https://github.com/immunIT/drupwn',
        'Say Thanks!': 'https://github.com/immunIT/drupwn/stargazers',
        'Source': 'https://github.com/immunIT/drupwn',
        'Tracker': 'https://github.com/immunIT/drupwn/issues',
    },

    packages=find_packages(),

    install_requires=['requests', 'veryprettytable', 'prompt_toolkit <= 2.0.7', 'pysocks', 'bs4'],
    python_requires='>=3',
    scripts=['drupwn']
)
