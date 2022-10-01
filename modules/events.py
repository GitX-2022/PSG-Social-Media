''' This code is Open Source Code for the GitX GitHub x PSG Tech Hackathon 2022.
    Team CodeHawk
    - Aaditya Rengarajan
    - Ajay Ramesh
    - S Karun Vikhash
    - Sanjay Kumaar Easwaran '''

import json
import datetime

def add(eve_name:str,
        start_date:str,
        end_date:str,
        sem_open:str,
        dep_open:list,
        or_name:str,
        desc:str,
        atnd=[]):
    with open ("data/events.json", "r") as source:
        obj = json.load(source)
    try:
        eve_code = str(int(obj["Events"][-1]["Event Code"])+1)
    except:
        eve_code = "1"
    data = {"Event Code": eve_code,"Event Name": eve_name, "Start Date": start_date, "End Date": end_date, "Semesters Open To": sem_open, "Departments Open To ": dep_open, "Organizer's Name": or_name, "Description":desc, "Attendees":atnd}
    obj["Events"].append(data)

    with open("data/events.json", "w") as dest:
        json.dump(obj, dest, indent=4)
    
def read():
    with open("data/events.json", "r") as source:
        obj = json.load(source)
    return obj["Events"]

def getEvent(eventID:int):
    with open("data/events.json", "r") as source:
        obj = json.load(source)

    for event in obj["Events"]:
        if str(eventID) == str(event["Event Code"]):
            return event

    with open("data/events.json", "w") as dest:
        json.dump({"Events":newEvents}, dest, indent=4)
def userEvents(user:str):
    with open("data/events.json", "r") as source:
        obj = json.load(source)
    myEvents = []
    for event in obj["Events"]:
        if user.upper() in event["Attendees"]:
            myEvents.append(event)
    return myEvents

def attendEvent(user:str, eventID:int):
    with open("data/events.json", "r") as source:
        obj = json.load(source)

    newEvents = []
    for event in obj["Events"]:
        if str(eventID) == str(event["Event Code"]):
            abc = event["Attendees"]
            abc.append(user)
            event["Attendees"] = abc
        print(event)
        newEvents.append(event)

    with open("data/events.json", "w") as dest:
        json.dump({"Events":newEvents}, dest, indent=4)

def delete(Event_Code):
    with open ("data/events.json", "r") as source:
        obj = json.load(source)
    for i in obj["Events"]:
        for j in list(i.keys()):
            for k in range(len(list(i.keys()))):
                if (i[j][k]["Event Code"] == Event_Code):
                    obj["Events"].remove(i)
     
    with open("data/events.json", "w") as dest:
        json.dump(obj, dest, indent=4)

def update(eve_id:str,
        eve_name:str,
        start_date:str,
        end_date:str,
        sem_open:str,
        dep_open:list,
        or_name:str,
        desc:str,
        atnd:list):
    
    delete(eve_id)
    add(eve_name,
        start_date,
        end_date,
        sem_open,
        dep_open,
        or_name,
        desc,
        atnd)