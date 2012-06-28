# -*- coding: utf-8 -*-
"""A/B Testing for Django

django-lean allows you to perform split-test experiments on your users.
In brief, this involves exposing 50% of your users to one implementation 
and 50% to another, then comparing the performance of these two groups 
with regards to certain metrics.
"""

from distutils.core import setup

description, long_description = __doc__.split('\n\n', 1)

setup(
    name='django-lean',
    version='0.2.4', #Remember to change src/django_lean/__init__.py.
    author='Akoha, Inc.',
    author_email='jdunck@votizen.com',
    description=('A framework for performing and analyzing split-test ' +
                 'experiments in Django applications.'),
    long_description=('django-lean provides a framework for implementing split-test ' +
                      'experiments in JavaScript, Python, or Django template ' +
                      'code along with administrative views for analyzing ' +
                      'the results of those experiments.'),
    license='BSD',
    platforms=['any'],
    url='http://github.com/votizen/django-lean/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    package_dir = {'': 'src'},
    packages=[
        'django_lean',
        'django_lean.experiments',
        'django_lean.experiments.management',
        'django_lean.experiments.management.commands',
        'django_lean.experiments.migrations',
        'django_lean.experiments.templatetags',
        'django_lean.experiments.tests',
        'django_lean.lean_analytics',
        'django_lean.lean_retention',
        'django_lean.lean_retention.migrations',
        'django_lean.lean_retention.tests',
        'django_lean.lean_segments',
        'django_lean.lean_segments.management',
        'django_lean.lean_segments.management.commands',
    ],
    package_data={
        'django_lean.experiments': ['media/experiments/*.js',
                                    'templates/experiments/*.html',
                                    'templates/experiments/include/*.html'],
        'django_lean.experiments.tests': ['data/*.json'],
    },
    install_requires=['django >= 1.0'],
    tests_require=['BeautifulSoup', 'mox'],
)
