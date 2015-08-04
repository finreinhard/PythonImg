__author__ = 'freinhard'

from PyPDF2 import PdfFileReader, PdfFileWriter;

input = PdfFileReader(open('bilder0.pdf' , 'rb'));

x = 344
y = 792

output = PdfFileWriter();



output.addPage(input.getPage(0));

output.getPage(0).mediaBox.upperRight = (
    output.getPage(0).mediaBox.getUpperRight_x() / 5,
    output.getPage(0).mediaBox.getUpperRight_y() / 5
)

outputStream = file("st.pdf", "wb");
output.write(outputStream);