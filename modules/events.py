import json
import datetime

def add(eve_code, eve_name, start_date, end_date, sem_open, dep_open, or_name, desc, atnd):
    with open ("Hackathon/JSON/events.json", "r") as source:
        obj = json.load(source)
    eve_code = str(int(obj["Events"][-1]["Event Code"])+1)
    data = {"Event Code": eve_code,"Event Name": eve_name, "Start Date": start_date, "End Date": end_date, "Semesters Open To": sem_open, "Departments Open To ": dep_open, "Organizer's Name": or_name, "Description":desc, "Attendees":atnd}
    obj["Events"].append(data)

    with open("Hackathon/JSON/events.json", "w") as dest:
        json.dump(obj, dest, indent=4)
    
def read():
    with open("Hackathon/JSON/events.json", "r") as source:
        obj = json.load(source)
    for i in (obj["Events"]):
        print(i)

def delete(Event_Code):
    with open ("Hackathon/JSON/events.json", "r") as source:
        obj = json.load(source)
    for i in obj["Events"]:
        for j in list(i.keys()):
            for k in range(len(list(i.keys()))):
                if (i[j][k]["Event Code"] == Event_Code):
                    obj["Events"].remove(i)
     
    for i in obj["Events"]:
        print(i)
    with open("Hackathon/JSON/events.json", "w") as dest:
        json.dump(obj, dest, indent=4)

def update(Event_Code):
    with open ("Hackathon/JSON/events.json", "w") as source:
        obj = json.load(source)
    for i in obj["Events"]:
        print("Hello World")

def update(eve_code):
    
    with open("Hackathon/JSON/events.json", "r") as source:
        obj = json.load(source)
    for i in (obj["Events"]):
        if(i["Event Code"] == eve_code):
            i["Attendees"].append(input())
            i["Event Name"] = input()
            i["Event Code"]=input()
            i["Event Name"]=input()
            i["Start Date"]=input()
            i["End Date"]=input()
            i["Semesters Open To"]=input()
            i["Departments Open To"]=input()
            i["Organizer's Name"]=input()
            i["Description"]=input()

    with open("Hackathon/JSON/events.json", "w") as dest:
        json.dump(obj, dest, indent=4)
delete(input())
