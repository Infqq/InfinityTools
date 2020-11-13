import setuptools

setuptools.setup(
    name="exrates",
    version="1.0.0",
    author="infqq",
    description="Tool for Rates",
    url="https://github.com/Infqq/exrates",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pycbrf~=0.4.0"
    ]
)
