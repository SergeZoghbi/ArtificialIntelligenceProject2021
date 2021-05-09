import PIL
from PIL import Image, ImageTk


def resize_image(image):
    my_width = 350
    w_percent = (my_width / float(image.size[0]))
    h_size = int((float(image.size[1]) * float(w_percent)))
    image = image.resize((my_width, h_size), PIL.Image.ANTIALIAS)
    return image
