from setuptools import setup, find_packages


setup(
    name='findmyfile',         # How you named your package folder (MyLib)
    packages=find_packages(),   # Chose the same as "name"
    version='0.3.0',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='This package allows you to search a directory for documents that match keywords',
    author='Sanjin Dedic',                   # Type in your name
    author_email='sanjindedic8@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/Sanjin84/findmyfile',
    # I explain this later on
    download_url='https://github.com/Sanjin84/findmyfile/archive/refs/tags/v_01.tar.gz',
    # Keywords that define your package best
    keywords=['file search', 'find file', 'search directory'],
    entry_points={
        'console_scripts': [
            'fmf = findmyfile.main:main',
        ],
    },
    install_requires=[
        # Add your dependencies here
        'PyMuPDF',
        'python-docx',
        'python-pptx',
        'pandas',
        'openpyxl',
        'xlrd'
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
