from setuptools import setup, find_packages

setup(
    name="fsearchpy",
    version="0.04",
    author="Dawood",
    description="This package searches for a specified text pattern in various documents, including office and PDFs and prints results including file name, path and size while displaying progress and completion time",
    packages=find_packages(),
    install_requires=["pymupdf", "pandas", "numpy", "python-pptx", "python-docx"],
    entry_points={
        "console_scripts": [
            "fsearchpy = fsearchpy.fsearchpy:main",
        ]
    },
    python_requires='>=3.8',
)