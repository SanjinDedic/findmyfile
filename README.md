# findmyfile

`findmyfile` is a Python package that allows you to search for keywords in various file types within a directory. It supports the following file types: .pptx, .docx, .xlsx, .pdf, and .txt. Additionally, this package provides a progress bar to visualize the search progress.

## Features

- Search for one or multiple keywords within supported file types
- Visualize the search progress with a progress bar
- Print the names of matching files and unreadable files
- Retrieve a list of matching file paths

## Installation

To use this package, simply copy the provided code into a Python script file (e.g., `findmyfile.py`) and run the script.

## Usage

```python
from findmyfile import FilesDB

db = FilesDB(path="your_directory_path")
db.search(keyword="keyword1", keyword2="keyword2")
```

Replace your_directory_path, keyword1, and keyword2 with the desired directory path and keywords you wish to search for.

You can also run the script from the command line:

python findmyfile.py -path "your_directory_path" -keyword1 "keyword1" -keyword2 "keyword2"

Replace your_directory_path, keyword1, and keyword2 with the desired directory path and keywords you wish to search for.

## Classes and Methods

The package contains the following classes:

- File: Base class representing a generic file
- PptxFile: Class representing a PowerPoint (.pptx) file
- DocxFile: Class representing a Word (.docx) file
- XlsxFile: Class representing an Excel (.xlsx) file
- TxtFile: Class representing a text (.txt) file
- PdfFile: Class representing a PDF (.pdf) file
- ProgressBar: Class for displaying a progress bar during file loading and searching
- FilesDB: Class that stores file data and provides search functionality

Each file type class inherits from the base File class and overrides the read() method to read the respective file format. The FilesDB class provides methods to search for keywords within the stored files and print the search results.

For a detailed explanation of the classes and methods, refer to the docstrings within the code.

## License

This package is free to use and modify.
