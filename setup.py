from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="1.2.3",
    packages=find_packages(),
    install_requires=[
        "setuptools~=68.1.2"
    ],
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:main",
        ],
    },
    author="Daniel Zeltner",
    author_email="daniel.zeltner@fau.de",
    description="a tool for simple math questions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/drentlez/dsss_homework_2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License",
    ]
)
