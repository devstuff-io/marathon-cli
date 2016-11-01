import ast
import re
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('marathon_cli/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(
        _version_re.search(f.read().decode('utf-8')).group(1)
    ))


setup(
    name='marathon-cli',
    version=version,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    description='command line utility for marathon api requests',
    long_description='command line utility for marathon api requests',
    url='https://github.com/meganlkm/marathon-cli',
    author='meganlkm',
    author_email='megan.lkm@gmail.com',
    keywords=['mesos', 'marathon', 'utility'],
    install_requires=[
        'click==6.6',
        'Jinja2==2.8',
        'jmespath==0.9.0',
        'pretty-json==1.0.1',
        'requests==2.11.1',
        'spylogger[pretty]==1.1.2',
    ],
    entry_points={
        'console_scripts': [
            'marathon=marathon_cli:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: System :: Software Distribution',
        'Topic :: Utilities'
    ]
)
