import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [i.strip() for i in open("requirements.txt").readlines()]

setuptools.setup(
    name='pagarme-surfmappers',
    version='1.3.0',
    description='Simple Pagar.me module made by Surfmappers.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/YuriAlessandro/pagarme-surfmappers',
    author='Yuri Alessandro Martins',
    author_email='yuri@surfmappers.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
