from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf") ]

for pdf in files:
    merger.append(pdf)
    
merger.write("F:/Python/CWH_Python/Python_Day82/merged-pdf.pdf")
# merger.write("merged-pdf.pdf")
merger.close()