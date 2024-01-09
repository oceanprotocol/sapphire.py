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
    name="sapphire.py",
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(
        include=[
            "sapphirepy",
        ]
    ),
    url="https://github.com/oceanprotocol/sapphirepy",
    version="0.2.2",
    zip_safe=False,
    data_files=[
        (
            "sapphirepy_bin",
            ["bin/sapphirewrapper-amd64.dylib", "bin/sapphirewrapper-arm64.dylib", "bin/sapphirewrapper-amd64.so", "bin/sapphirewrapper-arm64.so", "bin/sapphirewrapper-amd64.dll"],
        )
    ],
)
