from PIL import Image, ImageFont, ImageDraw
def cgen(subtext,name,date,logo):
    subfont = ImageFont.truetype("times new roman.ttf", 30)
    namefont = ImageFont.truetype("morganchalk.ttf", 80)
    datefont= ImageFont.truetype("verdana.ttf",30)
    
    #max length limit for any input is 30
    subtext=subtext.upper()
    
    my_image=Image.open("ctemplate.png")#background template is subject to change
    cimage=Image.open(logo)
    cimage=cimage.resize((150,150))
    image_editable = ImageDraw.Draw(my_image)
    #image_editable.text((530,200), title_text, (100, 100, 100), font=title_font)#text colours are subject to change
    image_editable.text((620,120),subtext, (39, 52, 82),anchor="ms",font=subfont)
    image_editable.text((620,558), name, (0, 0, 0), anchor="ms",font=namefont)
    image_editable.text((470,760), date, (0, 0, 0),anchor="ms", font=datefont)
    my_image.paste(cimage,(950,50))
    my_image.save("ticketrengaaaaaaa.png")#certificate name is also subject to change
    #my_image.show()
'''subtext="abcdefghijklmnopqrstuvwxyz12345"
name="Sanjay Kumaar Eswaran"
date="06-03-2022"
logo="clublogo.png"'''
#cgen(subtext,name,date,logo)
