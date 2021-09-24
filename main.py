"""__config.py: Config manipulation."""
__author__ = "Zain ul Abdin"
__license__ = "GPL-3"
__version__ = "1.0.0"
__maintainer__ = "Zain ul Abdin"
__email__ = "zulabdin21@gmail.com"
__status__ = "Production"

import tabula
import os


def exists(file_name):
    """
        checks if file exists in the path or not.
        Args:
             file_name: name of file to open/check.
         Returns:
             boolean.
         Raises:
             None.
    """

    if os.path.exists(file_name):
        return True
    return False


def get_table(file_name: str, pages='all', is_multiple_table=False):
    """
        gives table read from pdf as DataFrame.
        Args:
             file_name: name of file to open/check.
             pages: number of pages to read
             is_multiple_table: true if read multiple tables else false
         Returns:
             Pandas DataFrame.
         Raises:
             None.
    """

    if exists(file_name):
        return tabula.read_pdf("bankStatement.pdf", pages=pages, multiple_tables=is_multiple_table)
    return "File does not exists"


def to_csv(file_name: str, output_file: str, format_='csv', pages='all'):
    """
        checks if file exists in the path or not.
        Args:
             file_name: name of file to open/check.
             output_file: file name to store as csv.
             format_: format of file to save as.
             pages: number pages to convert to csv.
         Returns:
             string.
         Raises:
             None
    """

    if exists(file_name) and output_file.endswith(".pdf"):
        tabula.convert_into(file_name, output_file, format=format_, pages=pages)
    else:
        return "Failed! File does not exists"
    return "Operation succeeded."


print("done")
