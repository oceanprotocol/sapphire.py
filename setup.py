from setuptools import find_packages, setup

readme = ""

setup(
    author="oceanprotocol",
    author_email="devops@oceanprotocol.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
    ],
    description="Sapphire transaction wrapper",
    install_requires=[],
    name="pdr-sapphire-wrapper",
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(
        include=[
            "sapphire_wrapper",
        ]
    ),
    url="https://github.com/oceanprotocol/pdr-sapphire-wrapper",
    version='0.1.4',
    zip_safe=False,
    data_files=[('bin', ['bin/sapphirewrapper.dylib', 'bin/sapphirewrapper.so'])]
)