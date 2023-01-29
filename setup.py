from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name='key_guard',
    version='0.0.1a',
    author='Kolade Gideon',
    license='MIT',
    maintainer_email='allaye@koladegideon.me',
    description='Privshield is A helper tool to help prevent public disclosure of sensitive information, '
                'such as passwords, API keys, and tokens.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Allaye/privshield',
    py_modules=['privshield'],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        shield_cli=shield_cli:cli
    '''
)
