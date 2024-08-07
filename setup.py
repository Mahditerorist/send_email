from setuptools import setup, find_packages

def read_file(filename):
    with open(filename, encoding='utf-8') as f:
        return f.read()

setup(
    name='send_email',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
        'urllib3',
    ],
    include_package_data=True,
    description='A simple library to send emails using API from api-free.ir',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/Mahditerorist/send_email',
    author='Your Name',
    author_email='your-email@example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
