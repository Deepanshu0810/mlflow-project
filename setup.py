import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.1"

REPONAME = "mlflow-project"
AUTHOR = "Deepanshu0810"
AUTHOR_EMAIL = "deepanshu0810@gmail.com"
SRCREPO = "mlflowProject"

setuptools.setup(
    name=REPONAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="An end-to-end ML project with mlflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPONAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPONAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
