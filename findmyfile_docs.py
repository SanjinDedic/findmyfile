class File:
    """This class represents a file with properties such as path, name, extension, readable, and data.
    It also has methods to print and search the data in the file.

    Attributes:
    path (str): The path of the file.
    name (str): The name of the file, extracted from the path.
    extension (str): The extension of the file, default is ".txt".
    readable (bool): A flag indicating if the file is readable or not, default is True.
    data (str): The data in the file.
    """

    def __init__(self, path, extension=".txt"):
        """The constructor for the File class.
        Args:
        path (str): The path of the file.
        extension (str): The extension of the file, default is ".txt".
        """
        self.path = path
        self.name = os.path.basename(self.path)
        self.extension = extension
        self.readable = True
        self.data = ""

    def print(self):
        """This method prints the data in the file."""
        print(self.data)

    def search(self, keyword, keyword2=None):
        """This method searches for a keyword or a combination of keywords in the file data.
        Args:
        keyword (str): The keyword to be searched.
        keyword2 (str): The second keyword to be searched, default is None.

        Returns:
        bool: True if the keyword(s) is found in the file data, False otherwise.
        """
        info = self.data.lower()
        if keyword2:
            return keyword.lower() in info and keyword2.lower() in info
        else:
            return keyword.lower() in info


class PptxFile(File):
    """This class represents a PowerPoint file and inherits from the File class.
    It has additional methods to read the data from the PowerPoint file.

    Attributes:
    path (str): The path of the file, inherited from the File class.
    name (str): The name of the file, inherited from the File class.
    extension (str): The extension of the file, default is ".pptx", inherited from the File class.
    readable (bool): A flag indicating if the file is readable or not, default is True, inherited from the File class.
    data (str): The data in the file, inherited from the File class.
    """

    def __init__(self, path, extension=".pptx"):
        """The constructor for the PptxFile class.
        Args:
        path (str): The path of the file.
        extension (str): The extension of the file, default is ".pptx".
        """
        super().__init__(path, extension)
        self.read()

    def read(self):
        """This method reads the data from the PowerPoint file."""
        try:
            data=''
            prs = Presentation(self.path)
            values=[shape.text for slide in prs.slides for shape in slide.shapes if hasattr(shape, "text")]
            data=' '.join(values)
            self.data = data
        except:
            self.readable = False

