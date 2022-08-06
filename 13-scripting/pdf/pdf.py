import PyPDF2
import sys

input = sys.argv[1:]


def pdf_compiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('combined.pdf')


pdf_compiner(input)
