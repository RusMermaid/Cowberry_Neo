import json
from PIL import Image as IMG
#import math
from Classes.Class_String import String
from Classes.Class_Encrypted_Image import EncryptedImage

str3 = String (r"""БРАТЬЯ МАУГЛИ... это — последний из рассказов о Маугли.""")
str3.str_to_full_img().image.save(r"maugli.png")
image = IMG.open(r"maugli.png")
g = EncryptedImage(image).decode()
print(g)