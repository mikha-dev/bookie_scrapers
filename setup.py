import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bookie-scrapers",
    version="0.0.134",
    author="Jonatan Almen",
    author_email="almen.jonatan@gmail.com",
    description="Simple Oddsportal Scraper",
    install_requires=['selenium'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/almenjonatan/bookie_scrapers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.7',
)
