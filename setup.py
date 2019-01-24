from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="WonderPy_node",
    version="0.0.1",
    author="Ralf Anton Beier",
    author_email="",
    description="Python ROS2 node for working with Wonder Workshop robots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avrabe/WonderPy_node",
    packages=find_packages(),
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: MacOS X",
        "Framework :: Robot Framework",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 2.7",
    ),
    keywords=['robots', 'dash', 'dot', 'cue', 'wonder workshop', 'robotics'],
    test_suite='test',
    zip_safe=True,
    install_requires=[
        "mock"
    ]
)
