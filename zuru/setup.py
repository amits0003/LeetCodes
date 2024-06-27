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
        # Add any dependencies your project needs here
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A command-line tool to list directory contents from JSON structure",
    url="https://github.com/yourusername/pyls",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
