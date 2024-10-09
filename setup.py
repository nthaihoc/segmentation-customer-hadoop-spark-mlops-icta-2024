import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "segmentation-customer-hadoop-spark-mlops-icta-2024"
AUTHOR_NAME = "Thai Hoc Nguyen, Xuan Thi Tran"
SRC_REPO = "icta"
AUTHOR_EMAIL = "thaihoc.ictu@gmail.com, ttxuan@ictu.edu.vn"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Segmentation Customer Using Kmeans Clustering Combine Hadoop & Spark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/nthaihoc/{REPO_NAME}/",
    project_url={
       "Bug Tracker": f"https://github.com/nthaihoc/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)