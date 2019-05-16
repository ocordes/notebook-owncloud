import setuptools

setuptools.setup(
    name="notebook-owncloud",
    version='0.0.1',
    url="https://github.com/ocordes/notebook-owncloud",
    author="Oliver Cordes",
    description="Jupyter extension to enable user sync with ownCloud accounts",
    packages=setuptools.find_packages(),
    install_requires=[
        'notebook',
    ],
    package_data={'notebook_owncloud': ['static/*']},
)
