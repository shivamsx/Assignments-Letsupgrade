# Program to add text to our image .

from PIL import Image, ImageDraw, ImageFont


def add_text(selection, filename):
    img = Image.open("../static/IMG/"+filename)
    width, height = img.size
    write = ImageDraw.Draw(img)
    text = selection
    if len(text) <= 20:
        # Here we will add fonts to our text
        font = ImageFont.truetype('../static/FONT/consolas.ttf', 40)
        textwidth, textheight = write.textsize(text, font)
        margin = 325
        x = width - textwidth - margin / 1.8
        y = height - textheight - margin
        write.text((x, y), text, font=font, fill='#000000')
        img.save('../static/IMG/output.jpg')
        final_image = Image.open("../static/IMG/output.jpg")
        final_image.show()
    elif 21 <= len(text) <= 30:
        # Here we will add fonts to our text
        font = ImageFont.truetype('../static/FONT/consolas.ttf', 28)
        textwidth, textheight = write.textsize(text, font)
        margin = 325
        x = width - textwidth - margin / 1.8
        y = height - textheight - margin
        write.text((x, y), text, font=font, fill='#000000')
        img.save('../static/IMG/output.jpg')
        final_image = Image.open("../static/IMG/output.jpg")
        final_image.show()
    else:
        font = ImageFont.truetype('../static/FONT/consolas.ttf', 17)
        textwidth, textheight = write.textsize(text, font)
        margin = 325
        x = width - textwidth - margin / 1.8
        y = height - textheight - margin
        write.text((x, y), text, font=font, fill='#000000')
        img.save('../static/IMG/output.jpg')
        final_image = Image.open("../static/IMG/output.jpg")
        final_image.show()
# keep your image in static/IMG folder


text_here = input("Enter the text you want to add into the image : ")
name = input("Enter name of your image with format : ")
add_text(text_here, name)
