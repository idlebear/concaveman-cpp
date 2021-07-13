from distutils.core import setup

setup(
    name='concaveman',
    version='0.1dev',
    packages=['concaveman', ],
    package_dir={'': '.'},
    package_data={'': ['libconcaveman.so']},
    license='BSD 2-Clause License',
    long_description=open('README.txt').read(),
)
