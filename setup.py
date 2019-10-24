import setuptools

with open("README.rst", "r") as fh:
    long_desc = fh.read()

setuptools.setup(
    name='cia-serve',
    version='0.0.1',
    author='Skye Doto',
    author_email='skye@doto.works',
    description='Small HTTP Server to host CIA files for install with FBI',
    long_description=long_desc,
    long_description_content_type='text/x-rst',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.4'
)
