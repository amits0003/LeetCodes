from setuptools import setup, find_packages

setup(
    name="pyls",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyls=pyls.main:main',
        ],
    },
    install_requires=[
        "setuptools", "Wheel"
    ],
    author="Amit",
    description="A command-line tool to list directory contents from JSON structure",
    classifiers=[
        "Programming LanguagePython3"
    ],
    python_requires='>=3.8',
)
