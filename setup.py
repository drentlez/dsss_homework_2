from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="1.2.3pi",
    packages=find_packages(),
    install_requires=[],  # Hier ggf. Abhängigkeiten ergänzen
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:main",
        ],
    },
    author="Dein Name",
    author_email="deine.email@example.com",
    description="Ein CLI-Tool für Mathe-Übungen",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dein-benutzername/math_quiz",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
