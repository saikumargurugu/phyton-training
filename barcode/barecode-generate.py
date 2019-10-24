
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
StringSrart= 40
LineStart= 10
lineEnd=600
c.setFont("Courier", 20)
c.drawString(480,765,"impromed")
c.line(LineStart,759,lineEnd,760)
c.line(LineStart,759,lineEnd,760)
c.setFont("Courier", 28)
c.drawString(StringSrart,735,"Antech")
c.drawString(StringSrart,715,"Diagnostics")
c.line(LineStart,705,lineEnd,704)
c.line(LineStart,705,lineEnd,704)
c.setFont("Courier", 16)
c.drawString(StringSrart, 690, "Account ID:")
c.drawString(500,687,str(k))
c.drawString(StringSrart, 675, "Heritage Animal Hospital, Ltd.")
c.drawString(StringSrart, 660, "W6415 Greenville Dr")
c.drawString(StringSrart, 645, "Greenville, WI 54942")
c.drawString(StringSrart, 630, "Phone:")
c.line(LineStart,625,lineEnd,626)
c.line(LineStart,625,lineEnd,626)
c.setFont("Courier", 14)
c.drawString(StringSrart, 610, "clientNumber:")
c.drawString(StringSrart, 595, "Doctor")
c.drawString(300, 595, "Species:")
c.drawString(StringSrart, 580, "Owner Last Name")
c.drawString(300, 580, "Breed:")
c.drawString(StringSrart, 565, "Owner First Name")
c.drawString(300, 565, "Sex:")
c.drawString(StringSrart, 550, "Pet Name")
c.drawString(300, 550, "Age:")
c.line(LineStart,545,lineEnd,547)
c.line(LineStart,545,lineEnd,547)
c.drawString(StringSrart, 533, "Order Tests")
c.drawString(75, 520, "code")
c.drawString(225, 520, "Description")
c.line(65,515,lineEnd,514)
c.line(65,515,lineEnd,514)
c.drawString(65, 502, "FBX")
c.drawString(225, 502, "Surgical Biopsy")
c.line(LineStart,495,lineEnd,496)
c.line(LineStart,495,lineEnd,496)

c.drawString(StringSrart, 480, "Container Size/Number Submitted:")
c.drawString(StringSrart, 465, "Number of Specimens Submitted:")
c.drawString(StringSrart, 450, "Special Stain:")
c.drawString(StringSrart, 435, "Requested Pathologists:")
c.drawString(StringSrart, 420, "Source/Site:")
c.drawString(StringSrart, 405, "Previous Biopsy/Cytology Accession:")
c.drawString(StringSrart, 390, "Type of Biopsy:")
c.drawString(StringSrart, 375, "All Tissues Submitted:")
c.drawString(StringSrart, 350, "Other Comments:")





form = c.acroForm
k='dataa'
c.drawString(10, 310, 'aa:')
form.checkbox(name='cb1', tooltip='Field cb1',
            x=30, y=310, buttonStyle='check',  
            borderColor=magenta, fillColor=pink, 
            textColor=blue)

c.drawString(70, 310, 'bb:')
form.checkbox(name='cb2', tooltip='Field cb2',
            x=90, y=310, buttonStyle='check',  
            borderColor=magenta, fillColor=pink, 
            textColor=blue)

c.drawString(140, 310, 'cc:')
form.checkbox(name='cb3', tooltip='Field cb3',
            x=180, y=310, buttonStyle='check',  
            borderColor=magenta, fillColor=pink, 
            textColor=blue)

c.drawString(220, 310, 'dd:')
form.checkbox(name='cb4', tooltip='Field cb4',
            x=240, y=310, buttonStyle='check',  
            borderColor=magenta, fillColor=pink, 
            textColor=blue)

c.drawString(260, 310, 'ee:')
form.checkbox(name='cb5', tooltip='Field cb5',
            x=280, y=310, buttonStyle='check',  
            borderColor=magenta, fillColor=pink, 
            textColor=blue, checked=True)



c.save()