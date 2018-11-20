import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [i.strip() for i in open("requirements.txt").readlines()]

setuptools.setup(
    name='pagarme-surfmappers',
    version='1.0',
    description='Simple Pagar.me module made by Surfmappers.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Yuri Alessandro Martins',
    author_email='yuri@surfmappers.com',
    url='https://github.com/YuriAlessandro/pagarme-surfmappers',
    install_requires=requires,
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
    ],
)
