from setuptools import setup, find_packages

setup(
    name='send_email',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'urllib3',
    ],
    include_package_data=True,
    description='A simple library to send emails using API from api-free.ir',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mahditerorist/send_email',
    author='Mahdi Ahmadi',
    author_email='mahdiahmadi.1208@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
