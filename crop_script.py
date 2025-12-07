from PIL import Image, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

try:
    img = Image.open("header_slim.png")
    cropped_img = trim(img)
    cropped_img.save("header_final.png")
    print("Image cropped successfully to header_final.png")
except Exception as e:
    print(f"Error cropping image: {e}")
