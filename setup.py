import setuptools

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

test_requirements = [
    'pytest', 'coverage', "pytest-cov"
]


setuptools.setup(
    name="xicor",
    author="Phoenix Logan",
    author_email="phoenix.logan@czbiohub.org",
    maintainer="Pranathi Vemuri",
    maintainer_email="pranathi93.vemuri@gmail.com",
    description="xi correlation for tied data",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/czbiohub/xicor/",
    packages=setuptools.find_packages(
        exclude=[
            "tests",
            "*.tests",
            "*.tests.*",
            "tests.*",
            "test_*"]),
    include_package_data=True,
    install_requires=requirements,
    setup_requires=[
        "setuptools>=38.6.0", "setuptools_scm", 'setuptools_scm_git_archive'],
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    use_scm_version={
        'write_to': 'xicor/version.py'},
    test_suite='tests',
    extras_require={'test': test_requirements}
)
