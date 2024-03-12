import PyPDF2

pdf_files = ["css certificate.pdf","python_basic certificate.pdf"]
merger = PyPDF2.PdfMerger()
for file_name in pdf_files:
    PdfFile = open(file_name,'rb')
    pdfReader = PyPDF2.PdfReader(PdfFile)
    merger.append(pdfReader)
PdfFile.close()
merger.write('merged.pdf')


