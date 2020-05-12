import PyPDF2

template = PyPDF2.PdfFileReader(open('PDFs/MergedFile.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('PDFs/wtr.pdf', 'rb'))
output_file = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output_file.addPage(page)

    with open('WatermarkedFile.pdf', 'wb') as file1:
        output_file.write(file1)
