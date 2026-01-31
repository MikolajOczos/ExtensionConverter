from tkinter import *
from docx2pdf import *
from pathlib import *
import os as os
import tkinter as tk


class WordToPdf:
    def __init__(self, inputdoc):
        self.inputdoc = os.path.dirname(inputdoc)
        print(os.path.exists(self.inputdoc))

    def change(self):
        outputdoc = convert(self.inputdoc)
        return print(f"Nazwa zmienionego pliku to {outputdoc}")

class PdfToWord:
    def __init__(self, inputdoc):
        self.inputdoc = inputdoc

    def change(inputdoc):
        file = open(f"{inputdoc}", "w+")
        outputdoc = convert(file)
        return outputdoc

f1 = WordToPdf("cw2oczos.docx")
f1.change()


















































