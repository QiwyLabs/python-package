import io
from setuptools import setup



with io.open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="python_module",
    author="Username",
    version="1.0.0",
    license="None",
    url="https://github.com/",
    description="My Python module", 
    packages=["python_module"], 
    author_email="author@email.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False
)