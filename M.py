from PyPDF2 import PdfFileMerger
import glob

pdfs = sorted(glob.glob('*.pdf'))

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('mergedfile.pdf', 'wb') as fout:
    merger.write(fout)
