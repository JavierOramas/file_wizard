import setuptools

with open('readme.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='file-wizard',
    version='0.0.3',
    description='python package to manage files to avoid repetitive tasks such as move or delete', 
    author='Javier Oramas López',
    author_email='javiale2000@gmail.com',
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    url='https://github.com/JavierOramas/file-wizard', 
    # install_requires=['typer'],
    py_modules=['script'],
    license='MIT LICENSE',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License ',
        'Operating System :: OS Independent',  
    ],
)