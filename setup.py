from setuptools import setup
from codecs import open
from os import path


BASE = path.abspath(path.dirname(__file__))


with open(path.join(BASE, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-multiple-domains',
    version='0.0.1',
    url='https://github.com/qlio/django-multiple-domains',
    author='Bulgantamir Gankhuyag',
    author_email='mr.unagaldai@gmail.com',
    description="Django middleware for serving single Django instance in multiple domains with different urls.",
    packages=[
        'multidomain',
    ],
    include_package_data=True,
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='django url domain host multi',
)
