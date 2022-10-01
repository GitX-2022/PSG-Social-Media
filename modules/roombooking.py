import json

def update(rn,p):
    with open("rooms.json","r") as file:
        a=json.load(file)
    for i in a:
        if(i["room_no"]==rn):
            i["purpose"]=p
    with open("rooms.json","w") as file:
        json.dump(a,file)

def deletebooking(rn):
    with open("rooms.json","r") as file:
        a=json.load(file)
    for i in a:
        if(i["room_no"]==rn):
            i["purpose"]=""
    with open("rooms.json","w") as file:
        a=json.dump(file)

def addbooking(rn,dt,p):
    with open("rooms.json","r") as file:
        a=json.load(file)
    a.append({"room_no":rn,"date_time":dt,"p":purpose})
    with open("rooms.json","w") as file:
        a=json.dump(file)