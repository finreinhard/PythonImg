__author__ = 'freinhard'

import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image

filename = './BildB.jpg'

def get_python_image():
    """ Get a python logo image for this example """
    if not os.path.exists(filename):
        response = open('BildA.jpg', 'r');
        f = open(filename, 'w')
        f.write(response.read())
        f.close()

get_python_image()

doc = SimpleDocTemplate("image.pdf", pagesize=letter)
parts = []
parts.append(Image(filename))
doc.build(parts)
