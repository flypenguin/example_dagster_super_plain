from setuptools import find_packages, setup

# mostly stolen from example project.

setup(
    name="tm_dagster_playground_1",
    version="1!0+dev",
    author="The Me",
    author_email="ab@a3b3.de",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["test"]),
    package_data={"project_fully_featured": ["hacker_news_dbt/*"]},
    install_requires=[
        "dagster==1.1.20",
    ],
    extras_require={
        "dev": ["dagit==1.1.20", "pytest", "black[d]"],
        "tests": ["mypy", "pylint", "pytest"],
    },
)
