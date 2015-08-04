__author__ = 'freinhard'

from PyPDF2 import PdfFileReader, PdfFileWriter;
import NameObject;

input = PdfFileReader(open('bilder0.pdf' , 'rb'));

x = 344
y = 792

output = PdfFileWriter();



output.addPage(input.getPage(0));

page = output.getPage(0);

page.__setitem__(NameObject('/Type'), NameObject('/Page'))
page.__setitem__(NameObject('/Parent'), NullObject())
page.__setitem__(NameObject('/Resources'), DictionaryObject())

page.__setitem__(NameObject('/MediaBox'),
                 RectangleObject([0, 0, 500, 500]))

outputStream = file("st.pdf", "wb");
output.write(outputStream);