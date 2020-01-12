import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bookie_scrapers-almenjonatan",
    version="0.0.1",
    author="Jonatan Almen",
    author_email="almen.jonatan@gmail.com",
    description="Simple Oddsportal Scraper",
    install_requires=['selenium', 'pandas'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/almenjonatan/bookie_scrapers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
