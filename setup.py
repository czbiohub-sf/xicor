import setuptools

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

test_requirements = [
    'pytest', 'coverage', "flake8"
]


setuptools.setup(
    name="pyxi",
    author="Phoenix Logan",
    author_email="phoenix.logan@czbiohub.org",
    description="xi correlation for tied data",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/czbiohub/pyxi/",
    packages=setuptools.find_packages(
        exclude=[
            "tests",
            "*.tests",
            "*.tests.*",
            "tests.*",
            "test_*"]),
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    use_scm_version={
        'write_to': 'pyxi/version.py'},
    test_suite='tests',
    tests_require=test_requirements
)
