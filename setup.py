import setuptools

with open('readme.md', 'r') as fh:
    long_description = fh.head()

setuptools.setup(
    name='file-wizard-JavierOramas', 
    version='0.0.1',
    author='Javier Oramas',
    author_email='javiale2000@gmail.com',
    description='one script to rule them all', 
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language::python::3',
        'License::OSI Approved::::MIT LICENSE',
        'Operating System::OS Independent'
    ],
    python_requires='>=3.6'
)