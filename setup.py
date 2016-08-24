from setuptools import setup, find_packages

desc = ''
with open('README.rst') as f:
    desc = f.read()

setup(
    name='maul',
    version='0.1.0',
    description=('Multi-type configuration library for Python'),
    long_description=desc,
    url='https://github.com/pyarmory/maul',
    author='John Vrbanac',
    author_email='john.vrbanac@linux.com',
    license='Apache v2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='configuration plugin multiple',
    packages=find_packages(exclude=['contrib', 'docs', 'spec*']),
    install_requires=['six', 'alchemize', 'pike'],
    extras_require={
        'yaml': ['pyyaml'],
        'consul': ['pyyaml', 'requests'],
    },
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [],
    },
)
