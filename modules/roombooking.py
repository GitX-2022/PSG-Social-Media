import json

''' This code is Open Source Code for the GitX GitHub x PSG Tech Hackathon 2022.
    Team CodeHawk
    - Aaditya Rengarajan
    - Ajay Ramesh
    - S Karun Vikhash
    - Sanjay Kumaar Easwaran '''

def update(rn,p):
    with open("data/rooms.json","r") as file:
        a=json.load(file)
    for i in a:
        if(i["room_no"]==rn):
            i["purpose"]=p
    with open("data/rooms.json","w") as file:
        json.dump(a,file)

def deletebooking(rn):
    with open("data/rooms.json","r") as file:
        a=json.load(file)
    for i in a:
        if(i["room_no"]==rn):
            i["purpose"]=""
    with open("data/rooms.json","w") as file:
        a=json.dump(file)

def addbooking(rn,dt,p,by):
    with open("data/rooms.json","r") as file:
        a=json.load(file)["rooms"]
    a.append({"room_no":rn,"date_time":dt,"purpose":p,"by":by})
    with open("data/rooms.json","w") as file:
        json.dump({"rooms":a},file, indent=4)

def viewbookings():
    with open(f"data/rooms.json") as f:
        rooms = json.load(f)
    return rooms.get("rooms")