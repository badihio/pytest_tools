import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pytest_tools',
    version='0.0.2',
    author='Ohad Badihi',
    description='Some nice tooling for pytest',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    py_modules=['pytest_tools'],
    package_dir={'': 'pytest_tools/src'},
    install_requires=[]
)
