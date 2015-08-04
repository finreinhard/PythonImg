__author__ = 'freinhard'
from PyPDF2 import PdfFileWriter, PdfFileReader;

from os import system;

output = PdfFileWriter();
input = PdfFileReader(open("test1.pdf", "rb"));

print "document1.pdf has", input.getNumPages(), "Page";

output.addPage(input.getPage(0));

output.addPage(input.getPage(0).rotateClockwise(90));


system("sips -s format pdf BildA.jpg --out test.pdf")

outputStream = file("PyPDF2-output.pdf", "wb")
output.write(outputStream)