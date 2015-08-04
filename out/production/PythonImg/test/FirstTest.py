__author__ = 'freinhard'

from os import path;
from os import system;
import argparse;
from PyPDF2 import PdfFileWriter, PdfFileReader;

parser = argparse.ArgumentParser(description='PDF aus Bildern');

parser.add_argument('files', metavar="F", type=str, nargs='+', help='Bilder, welche "konvertiert" werden');
parser.add_argument('target', metavar="T", type=str, nargs='+', help='Pfad der Ziel Datei!');

args = parser.parse_args();

files = [];

for x in range(0, len(args.files)):
    if path.isfile(args.files[x]):
        name = str.split(args.files[x], ".")[0];
        system("sips -s format pdf -s formatOptions best " + args.files[x] + " --out " + name + ".pdf");
        files.append(name + ".pdf");


output = PdfFileWriter();

for i in range(0, len(files)):
    picture = PdfFileReader(open(files[i], "rb"));

    page = picture.getPage(0);
    size = page.mediaBox;

    x = size[2];
    y = size[3];

    if x > y:
        page.rotateClockwise(90);
        x = size[3];
        y = size[2];
    scale = 595 / x;

    #if y*scale > 842:
     #   scale = 842 / y;

    x *= scale;
    y *= scale;
    x = round(x);
    y = round(y);

    print "Picture:", i, "X:", x, "Y:", y, "Scale:", scale;
    output.addPage(page);
    output.getPage(i).mediaBox.upperRight = (x, y);

outputStream = file(args.target[0], "wb");
output.write(outputStream);

for x in range(0, len(files)):
    system("rm " + files[x]);