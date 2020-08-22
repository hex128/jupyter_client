import setuptools

setuptools.setup(
    name='jupyter_client',
    version='0.0.1',
    author='hex128',
    author_email='me@hex128.io',
    description='Jupyter Notebook Server Client',
    url='https://github.org/hex128/jupyter_client',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'aiohttp[speedups]',
        'websockets',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
