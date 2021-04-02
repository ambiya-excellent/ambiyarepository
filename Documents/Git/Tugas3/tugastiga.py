from PIL import Image
import PIL

# Buka gambar sumber
img = Image.open('manusia.jpg')

border_im = PIL.Image.new('RGB', (img.width+20, img.height+20), 'yellow')
border_im.paste(img, (10, 10))
border_im.save('border.jpg')

