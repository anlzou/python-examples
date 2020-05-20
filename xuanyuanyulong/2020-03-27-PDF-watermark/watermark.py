#
# @Date        : 2020-05-11 21:04:44
# @LastEditors : anlzou
# @Github      : https://github.com/anlzou
# @LastEditTime: 2020-05-20 20:51:51
# @FilePath    : \python-examples\xuanyuanyulong\2020-03-27-PDF-watermark\watermark.py
# @Describe    :
#
import PyPDF2

inputName = "input.pdf"
watermarkName = "watermark.pdf"
outputName = "output.pdf"

pdfInput = PyPDF2.PdfFileReader(inputName)
watermark = PyPDF2.PdfFileReader(watermarkName).getPage(0)

pdfWriter = PyPDF2.PdfFileWriter()

# print(pdfInput.numPages)
# print(pdfInput.getNumPages())

for i in range(pdfInput.numPages):
    page = pdfInput.getPage(i)
    page.mergePage(watermark)
    pdfWriter.addPage(page)

with open(outputName, "wb") as f:
    pdfWriter.write(f)
