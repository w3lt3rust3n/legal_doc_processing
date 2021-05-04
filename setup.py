import setuptools
from document_processing.version import Version


setuptools.setup(name='theolex-document-processing',
                 version=Version('1.0.0').number,
                 description='Theolex document processing',
                 long_description=open('README.old.md').read().strip(),
                 author='Jawad Alaoui',
                 author_email='jawad.alaoui@theolex.io',
                 url='http://theolex-document-processing',
                 py_modules=['document_processing'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='theolex document processing package',
                 classifiers=['Packages', 'NLP'])
