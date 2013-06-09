from fred import __appname__, __version__
from setuptools import setup


long_description = ""

setup(
    name=__appname__,
    version=__version__,
    scripts=[],
    packages=[
        'fred',
    ],
    author="Paul Tagliamonte",
    author_email="tag@pault.ag",
    long_description=long_description,
    description='You got some \'splainin to do!',
    license="Expat",
    url="http://deb.io/",
    platforms=['any'],
)
