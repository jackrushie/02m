import PyPDF2
import sys
import os

filepath = './02m/PDF_editting/PDFs/'
inputs = os.listdir(filepath)

print(inputs)


def pdf_combined(filepath):
    merger = PyPDF2.PdfFileMerger()
    for pdf in os.listdir(filepath):
        if pdf.endswith((".pdf")):
            print(pdf)
        merger.append(f'{filepath}{pdf}')
    merger.write('MergedFile.pdf')


pdf_combined(filepath)
