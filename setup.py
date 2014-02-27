from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os

version = __import__('timberwyckfarm_com').__version__

install_requires = [
    'setuptools',
    'django>=1.6',
    'south>=0.8.2',
    'django-farm>=0.4.2',
    'django-notes>=0.2.2',
    'django-attributes==0.1.0',
    'psycopg2==2.4.3',
    'uuid==1.30',
    'smartypants==1.6.0.3',
]

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)

setup(
    name = "timberwyckfarm_com",
    version = version,
    url = 'http://bitbucket.org/powellc/timberwyckfarm_com',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "A website for Timberwyck Farm.",
    author = "Colin Powell",
    author_email = 'colin.powell@gmail.com',
    packages=find_packages(),
    install_requires = install_requires,
    include_package_data=True,
    zip_safe=False,
    tests_require=['tox'],
    cmdclass = {'test': Tox},
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_dir={
        'timberwyckfarm_com': 'timberwyckfarm_com',
    },
)
