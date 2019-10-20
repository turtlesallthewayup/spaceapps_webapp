import base64
from django.core.files.base import ContentFile
from PIL import Image
from base64 import decodestring
from io import BytesIO


def base64_to_file(link_base64):
    if not link_base64:
        return ''
    
    # ------------------------
    # img_format, img_str = link_base64.split(';base64,')
    # header, extension = img_format.split('/')
    # mime_type = header.split(':')[-1]
    # name = 'image_base64'
    # ------------------------


    # ------------------------
    # https://stackoverflow.com/questions/45122994/how-to-convert-base64-string-to-a-pil-image-object?rq=1
    # sg = base64.b64decode(msg)
    # buf = io.BytesIO(msg)
    # img = Image.open(buf)
    # ------------------------
    
    try:

        img_format, data = link_base64.split(';base64,')    
        return Image.open(BytesIO(base64.b64decode(data)))    
        
        # return ContentFile(base64.b64decode(img_str), name='{}.{}'.format(name, extension))
        
    except Exception as e:
        print(str(e))