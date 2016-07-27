#!/usr/bin/python

# Import from standard packages
import os
import sys

class resource_path():
    """
    This class allows to get the absolute path to the resource scripts. It works
    for development installation as well as for PyInstaller builds (.app, .exe).
    """

    def __init__(self, relative_path):
        self.relative_path = relative_path

    def return_path(self):
        """
        Get absolute path to resource, works for dev and for PyInstaller

        :return: relative path to be used to find all DICAT scripts
         :rtype: str
        """
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, self.relative_path)

        return os.path.join(os.path.abspath("."), self.relative_path)