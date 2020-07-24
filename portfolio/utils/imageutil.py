from PIL import Image

def check_image_png(image):
    if image.format == 'PNG':
        return True
    return False

def convert_to_png(image, file):
    image.save(file)

def convert(file):
    image = Image.open(file)
    new_file = file + '.png'
    check_image_png(image)
    convert_to_png(image, new_file)
    return new_file
    