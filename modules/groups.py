import json
import datetime

def send():
    with open ("#","r") as source:
        obj = json.load(source)

    Title = str(input())
    Description = str(input())
    Thumbnail = str(input())
    Languages = str(input())
    Members = str(input())
    Link_WhatsApp = str(input())
    Name = str(input())
    Date = str(datetime.datetime.now())[:-7]
    Description_1 = str(input())

    
    data = {"Code": str(int(obj["Groups"][-1]["Code"])+1),"Title": Title, "Description": Description, "Thumbnail": Thumbnail, "Languages (if Coding)": Languages, "Members": Members, "Link to WhatsApp Group": Link_WhatsApp,"Milestones":[{"Name": Name, "Date": Date, "Description": Description_1}]}
    obj["Groups"].append(data)

    with open("Hackathon/groups.json","w") as dest:
        json.dump(obj, dest, indent=4)
    
def read():
    with open("groups.json","r") as source:
        obj = json.load(source)
    for i in (obj["groups"]):
        print(i)

def delete(Code):
    with open ("Hackathon/groups.json", "r") as source:
        obj = json.load(source)
    for i in obj["Groups"]:
        if (i["Code"] == Code):
            obj["Groups"].remove(i)
    
    for i in obj["Groups"]:
        print(i)
    with open("Hackathon/groups.json", "w") as dest:
        json.dump(obj, dest, indent=4)

#send()
delete(input())