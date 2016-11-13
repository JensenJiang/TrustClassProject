from setuptools import setup, find_packages

INSTALL_REQUIREMENTS = [
    'Django',
    'djangorestframework',
    'django-oauth-toolkit',
    'django-simple-captcha',
    'mysqlclient',
]

CLASSFIERS = [
    'Development Status :: 1 - Planning',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3 :: Only',
]

setup(
    name='TrustClassProject',
    version='0.1',
    packages=find_packages(),
    install_requires=INSTALL_REQUIREMENTS,
    classifiers=CLASSFIERS,
    author='',
    author_email='',
    description='',
    keywords='',
    url='',
    license='',
)
