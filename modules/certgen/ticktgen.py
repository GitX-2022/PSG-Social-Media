from PIL import Image, ImageFont, ImageDraw
import PIL
def tgen(subtext,name,time,date,logo,event):
    #club logo should be given as png image
    #subtext is club name
    subfont = ImageFont.truetype("verdana.ttf", 55)
    namefont = ImageFont.truetype("verdana.ttf", 70)
    datefont= ImageFont.truetype("verdana.ttf",30)
    eventfont= ImageFont.truetype("morganchalk.ttf",60)
    img=Image.open("ticketbg.png")
    
    date=date+"  "+time
    
    cimage=Image.open(logo)
    cimage=cimage.resize((110,110))
    image_editable = ImageDraw.Draw(img)
    image_editable.text((170,45),subtext, (255, 255, 255),font=subfont)

    image_editable.text((170,115), date, (255, 255, 255), font=datefont)
    image_editable.text((170,215), name, (255, 255, 255),font=namefont)
    #image_editable.text((430,230), event, (0, 70, 0),font=namefont)
    img2  = Image.new( mode = "RGB", size = (350, 110), color = (0, 0, 0) )
    im_edit=ImageDraw.Draw(img2)
    im_edit.text((0,8),event,(255,255,255),font=eventfont)
    img.paste(cimage,(50,45))

    img2=img2.rotate(90,PIL.Image.NEAREST,expand=1)
    img.paste(img2,(870,30))
    img.save("tickettt.png")
    #img.show()
'''subtext="CLUB NAME"
name="21z201"#name limit is 6-8
time="12:20"
date="06-03-2022"
logo="clublogo.png"
event="HACKFEST"#event name limit is 12
tgen(subtext,name,time,date,logo,event)'''
