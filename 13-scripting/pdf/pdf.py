import PyPDF2

pdfFile = open('dummy.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
print(pdfReader.numPages)
page = pdfReader.getPage(0)
print(page.extractText())
pdfFile.close()
