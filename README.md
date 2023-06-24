# Cross Platform File System Search

This project consists of a series of Python classes that can be used to process, search, and display information from different file types (PowerPoint, Word, Excel, PDF, and Text) present in a given directory. 

This tool has been designed to explore a specified directory, read the data from the files present in the directory, and provide a method to search within the file content. It also maintains a count of files that were unreadable due to any issues.

## Dependencies

The following Python packages are used in this project:

- os
- sys
- fitz (PyMuPDF)
- python-docx
- python-pptx
- argparse
- pandas

Please make sure these packages are installed. If not, use the package manager [pip](https://pip.pypa.io/en/stable/) to install them.

```bash
pip install PyMuPDF python-docx python-pptx pandas
```

## Classes

The project comprises several classes:

1. **File**: This base class represents a generic file object. It holds the path, name, extension, and data of the file. It also provides methods to print the file data and search for keywords within the file data. The `read` method of this class should be overridden by each subclass to handle specific file types.

2. **PptxFile, DocxFile, XlsxFile, TxtFile, PdfFile**: These classes represent specific file types (PowerPoint, Word, Excel, Text, and PDF files, respectively). Each of them inherits from the base File class and overrides the `read` method to handle the specific file type.

3. **ProgressBar**: This class provides a simple progress bar which can be used to visualize the progress of long running operations.

4. **FilesDB**: This class represents a database of files. It explores a given directory path and creates an instance of the appropriate class for each supported file type (pptx, docx, xlsx, pdf, txt) it finds. It provides a method to search for keywords across all files in the database.

## Usage

This project can be utilized as a library in your project or as a standalone script. The usage would depend on the specific requirements of your project. 

An example of searching for keywords would be:

```python
fdb = FilesDB('your/directory/path')
fdb.search('your', 'keywords')
```

This will print the names of the files which contain all the keywords.

## Contributions

Contributions are always welcome! Please read the contribution guidelines first.

## License

[MIT](https://choosealicense.com/licenses/mit/)