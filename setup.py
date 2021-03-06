import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tsfeatures",
    version="0.1.0",
    author="Federico Garza",
    author_email="fede.garza.ramirez@gmail.com",
    description="features for time series",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FedericoGarza/tsfeatures",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "arch>=4.11",
        "entropy@git+https://github.com/raphaelvallat/entropy@v0.1.1",
        "pandas>=1.0.5",
        "scikit-learn>=0.23.1",
        "statsmodels>=0.11.1",
        "supersmoother>=0.4"
    ]
)
