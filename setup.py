from setuptools import setup

def readme():
    with open('README.md') as fin:
        return fin.read()

install_requires = [
    'requests>=2.2.0',
]

packages = [
    'scratchsession',
]

setup(
    name='scratchsession',
    version='1.0.0',
    author='yuwex',
    url='https://github.com/yuwex/scratchsession',
    description='A simple function for setting up scratch HTTP sessions.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    
    install_requires=install_requires,
    python_requires='>=3.7',
    packages=packages,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Education',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ]
)
