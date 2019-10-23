import barcode
import random
import json

n=random.randrange(1,1000000000000)
n=json.loads(json.dumps(n))
img= barcode.get_barcode_class('ean13')
img_bar=img(u'{}'.format(n))
file=open('2.JPEG ','wb')
img_bar.write(file)
