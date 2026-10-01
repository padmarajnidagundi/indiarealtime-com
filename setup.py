from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="indiarealtime",
    version="0.1.0",
    author="Padmaraj Nidagundi",
    author_email="padmaraj@indiarealtime.com",
    description="Python SDK for IndiaRealTime APIs - Live India data aggregator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/padmarajnidagundi/indiarealtime-com",
    project_urls={
        "Bug Tracker": "https://github.com/padmarajnidagundi/indiarealtime-com/issues",
        "Documentation": "https://docs.indiarealtime.com",
        "Source Code": "https://github.com/padmarajnidagundi/indiarealtime-com",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "python-dateutil>=2.8.2",
        "pytz>=2022.7",
        "click>=8.1.0",
        "tabulate>=0.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.990",
        ],
    },
    entry_points={
        "console_scripts": [
            "indiarealtime=indiarealtime.cli:main",
        ],
    },
)
