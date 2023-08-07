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
    name="sapphireyp",
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(
        include=[
            "sapphireyp",
        ]
    ),
    url="https://github.com/oceanprotocol/sapphireyp",
    version="0.1.13",
    zip_safe=False,
    data_files=[
        (
            "sapphireyp_bin",
            ["bin/sapphirewrapper.dylib", "bin/sapphirewrapper.so"],
        )
    ],
)
