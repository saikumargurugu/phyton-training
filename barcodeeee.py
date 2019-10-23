# import barcode
# import random
# print("in try")
# k = random.randrange(1, 1111111111111)
# print(k)
# img = barcode.get_barcode_class('ean13')
# img_bar = img(u'{}'. format(k))
# file = open('1.svg', "wb")
# img_bar.write(file)
# print("Done")
#
#from pdf417 import encode, render_image, render_svg
#
#text = """Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated."""
#
#codes = encode(text)
#image = render_image(codes) 
#image.save('barcode.jpg')
#svg = render_svg(codes)
#svg.write("barcode.svg")


# import code128

# code128.image("name gid d,f fd;gdfgbvln.x fjvc mjv k,njfcv, dcjfbfdgksdfvxdlfxkhgbxdfkjgvfkcghvdfcvvhnd,vjfbcfmnbgjkfdcjv mndcgbjkndfn bvk,gdvfjgfvkdjbdxfclgbhnlcfdjgbdfrguhikdrgfkrjdvgdkrfjugkfdgbh").save("Hello World.png")  # with PIL present

# with open("Hello World.svg", "w") as f:
#         f.write(code128.svg("Hello World"))


##################################
#          PDF CREATION          #
##################################
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import magenta, pink, blue, green
from reportlab.platypus import Table,TableStyle
c = canvas.Canvas('simple_checkboxes.pdf',pagesize=letter)
k=date.today()
c.setFont("Courier", 20)
c.drawString(480,765,"impromed")
c.line(0,759,1000,760)
c.line(0,759,1000,760)
c.setFont("Courier", 28)
c.drawString(10,735,"Antech")
c.drawString(10,715,"Diagnostics")
c.line(0,705,1000,704)
c.line(0,705,1000,704)
c.setFont("Courier", 16)
c.drawString(10, 690, "Account ID:")
c.drawString(500,687,str(k))
c.drawString(10, 675, "Heritage Animal Hospital, Ltd.")
c.drawString(10, 660, "W6415 Greenville Dr")
c.drawString(10, 645, "Greenville, WI 54942")
c.drawString(10, 630, "Phone:")
c.line(0,625,1000,626)
c.line(0,625,1000,626)
c.setFont("Courier", 14)
c.drawString(10, 610, "clientNumber:")
c.drawString(10, 595, "Doctor")
c.drawString(300, 595, "Species:")
c.drawString(10, 580, "Owner Last Name")
c.drawString(300, 580, "Breed:")
c.drawString(10, 565, "Owner First Name")
c.drawString(300, 565, "Sex:")
c.drawString(10, 550, "Pet Name")
c.drawString(300, 550, "Age:")
c.line(0,545,1000,547)
c.line(0,545,1000,547)
c.drawString(10, 533, "Order Tests")
c.drawString(65, 520, "code")
c.drawString(225, 520, "Description")
c.line(0,515,1000,514)
c.line(0,515,1000,514)
c.drawString(65, 502, "FBX")
c.drawString(225, 502, "Surgical Biopsy")
c.line(0,495,1000,496)
c.line(0,495,1000,496)

c.drawString(10, 480, "Surgical Biopsy")
c.drawString(10, 465, "Surgical Biopsy")
c.drawString(10, 450, "Surgical Biopsy")
c.drawString(10, 435, "Surgical Biopsy")
c.drawString(10, 420, "Surgical Biopsy")
c.drawString(10, 405, "Surgical Biopsy")
c.drawString(10, 390, "Surgical Biopsy")
c.drawString(10, 375, "Surgical Biopsy")


c.save()


# form = c.acroForm
# k='dataa'
# c.drawString(10, 650, 'Dog:')
# form.checkbox(name='cb1', tooltip='Field cb1',
#             x=110, y=645, buttonStyle='check',  
#             borderColor=magenta, fillColor=pink, 
#             textColor=blue, forceBorder=True)

# c.drawString(10, 600, 'Cat:')
# c.drawString(50, 600,k)
# form.checkbox(name='cb2', tooltip='Field cb2',
#             x=110, y=595, buttonStyle='cross',
#             borderWidth=2, forceBorder=True)

# c.drawString(10, 550, 'Pony:')
# form.checkbox(name='cb3', tooltip='Field cb3',
#             x=110, y=545, buttonStyle='star',
#             borderWidth=1, forceBorder=True)

# c.drawString(10, 500, 'Python:')
# form.checkbox(name='cb4', tooltip='Field cb4',
#             x=110, y=495, buttonStyle='circle',
#             borderWidth=3, forceBorder=True)

# c.drawString(10, 450, 'Hamster:')
# form.checkbox(name='cb5', tooltip='Field cb5',
#             x=110, y=445, buttonStyle='diamond',
#             borderWidth=None,
#             checked=True,
#             forceBorder=True)



