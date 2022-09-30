from PIL import Image , ImageFont, ImageDraw
#this is barebones certificate module will be developed later
def createcertificate(subtext,name):
    title_font = ImageFont.truetype("arial.ttf", 140)#text fonts are subject to change
    subfont = ImageFont.truetype("calibri.ttf", 80)
    namefont = ImageFont.truetype("verdana.ttf", 80)
    title_text = "CERTIFICATE"
    #subtext="CLUB NAME"
    #name="RENGA"
    my_image=Image.open("certificatebackground.png")#background template is subject to change
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((530,200), title_text, (100, 100, 100), font=title_font)#text colours are subject to change
    image_editable.text((740,480), subtext, (100, 200, 100), font=subfont)
    image_editable.text((800,680), name, (100, 200, 300), font=namefont)
    my_image.save("certificate.rgba")#certificate name is also subject to change
    my_image.show()


createcertificate("This is a cert", "Aad")
