from setuptools import setup, find_packages
setup(
  name = 'findmyfile',         # How you named your package folder (MyLib)
  packages = find_packages(),   # Chose the same as "name"
  version = '0.2.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This package allows you to search a directory for documents that match keywords',   # Give a short description about your library
  author = 'Sanjin Dedic',                   # Type in your name
  author_email = 'sanjindedic8@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Sanjin84/findmyfile',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Sanjin84/findmyfile/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['file search', 'find file', 'search directory'],   # Keywords that define your package best
  entry_points={
      "console_scripts": [
          "findmyfile = findmyfile.findmyfile:FilesDB",
      ]
  },
  install_requires=["pymupdf", "pandas", "numpy", "python-pptx", "python-docx"],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', 
    "Operating System :: OS Independent",  
  ],
  python_requires=">=3.6",
)