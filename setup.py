import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wagglepy",
    version="0.0.1",
    author="Wenyin Wei",
    author_email="wenyin.wei.ww@gmail.com",
    description="The wagglepy package consists of a collection of template notebooks and some utility functionality for drawing and analyzing the particle traces in the study of plasma physics. Wagglepy, however, does not restrict itself in particle-tracing, but would expand its application across ray-tracing, stochastic procedure and so on, all of which share the same essence, that is, the ordinary differential system.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WenyinWei/wagglepy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)