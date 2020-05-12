import PyPDF2

# read file as binary
with open('./02m/PDF_editting/PDFs/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    # Print Number of pages
    print(f'Number of pages: {reader.numPages}')
    # Print page details
    print(f'page details: {reader.getPage(0)}')
