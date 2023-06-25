# FMF (Find My File)

FMF is a powerful file management system that reads and searches text within files in various formats including PPTX, DOCX, XLSX, PDF, and TXT. It traverses the given directory and its sub-directories and reads the content of the supported files. It provides functionality to search for one or more keywords across all files.

---

## Installation

You can install FMF directly from the Python Package Index using pip. Open a terminal and run the following command:

```bash
pip install findmyfile
```

Please ensure that you have `pip` installed and that your Python environment is correctly set up.

After successful installation, you can use FMF as a library in your project or as a CLI command. 

You can find the findmyfile project on PyPi here: [findmyfile](https://pypi.org/project/findmyfile)

---

## Usage

### As a Library

FMF can be imported into your project as a library, and its classes can be used independently. Below are some usage examples:

**Example 1:** Reading a specific .docx file.

```python
from fmf import DocxFile

file = DocxFile('path/to/your/docxfile.docx')
file.read()
file.print()  # Prints first 100 characters of the file
```

**Example 2:** Searching keywords in a directory

```python
from fmf import FilesDB

db = FilesDB('path/to/directory')
db.search('keyword1', 'keyword2')
```

Sure, here is a reworded version:

### As a CLI Command

After installation, you can directly use the `fmf` command in your terminal. Here are some usage examples:

**Example 1:** Searching within files in the current directory

To search for keywords within the files of your current directory, use the following format:

```bash
fmf -w keyword1 keyword2
```

This command will search for `keyword1` and `keyword2` within the files of the directory you're currently in.

**Example 2:** Searching within files in a specific directory

If you want to search for keywords within a specific directory, include the `-path` argument followed by the path to the directory. Here's the format:

```bash
fmf -path "/path/to/directory" -w keyword1 keyword2
```

Replace `/path/to/directory` with the path to your desired directory. This command will then search for `keyword1` and `keyword2` within the files of the specified directory.

Please note that `fmf` does not search in subdirectories. If you want to search in a subdirectory, you need to specify it in the `-path` argument.

---

## Classes and Methods

**File**: The base class for all file types.

- **`create(path, extension)`**: A classmethod to create a new File object.

- **`print(chars=100)`**: Prints the first `chars` characters of the file's data.

- **`search_all(*keywords)`**: Returns True if all the given keywords are in the file's data.

- **`search_any(*keywords)`**: Returns True if any of the given keywords are in the file's data.

**PptxFile, DocxFile, XlsxFile, TxtFile, PdfFile**: Inherit from File and override the read method for their specific file type.

**ProgressBar**: A class to visualize the progress of loading files.

- **`print_progress(iteration)`**: Prints the progress bar at the given iteration.

**FilesDB**: A class to manage a collection of File objects.

- **`count_files()`**: Returns the count of all supported files in the path.

- **`add_file_data()`**: Adds File objects for all supported files in the path.

- **`search(*keywords)`**: Searches for keywords in all files and prints the names of files that contain all keywords.

---

## Command Line Arguments

- `-path`, `--source_path`: Takes the directory path as input. Default is the current directory.

- `-w`, `--words`: Takes any number of text patterns as input. Multiple keywords should be separated by space.

- `save`: Saves a log file in a folder.

- `verbose`: Shows the text found in the file.

---

## Dependencies

The FMF script requires the following Python libraries:

- os
- sys
- fitz (PyMuPDF)
- docx
- pptx
- argparse
- pandas

Make sure all dependencies are installed to successfully run the script.

## Contributions

Contributions are always welcome! Please read the contribution guidelines first.

## License

[MIT](https://choosealicense.com/licenses/mit/)