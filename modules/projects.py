import json
import datetime

def send():
    with open ("Hackathon/JSON/projects.json","r") as source:
        obj = json.load(source)

    Title = str(input())
    Description = str(input())
    Url = str(input())
    Thumbnail = str(input())
    Languages = str(input())
    Vaccancies = str(input())
    Members = str(input())
    M_Name = str(input())
    M_Date = str(datetime.datetime.now())[:-7]
    M_Description_1 = str(input())
    Me_Name = str(input())
    Me_Roll = str(input())

    
    data = {"Code": str(int(obj["Projects"][-1]["Code"])+1),"Title": Title, "Description": Description, "URL": Url, "Thumbnail": Thumbnail, "Languages (if Coding)": Languages, "Vaccinces": Vaccancies, "Members": [{"Name": Me_Name, "Roll_No.": Me_Roll}], "Milestones":[{"Name": M_Name, "Date": M_Date, "Description": M_Description_1}]}
    obj["Projects"].append(data)

    with open("projects","w") as dest:
        json.dump(obj, dest, indent=4)
    
def read():
    with open("Hackathon/JSON/projects.json","r") as source:
        obj = json.load(source)
    for i in (obj["Projects"]):
        print(i)

def delete(Code):
    with open ("Hackathon/JSON/projects.json", "r") as source:
        obj = json.load(source)
    for i in obj["Projects"]:
        if (i["Code"] == Code):
            obj["Projects"].remove(i)
    
    for i in obj["Projects"]:
        print(i)
    with open("Hackathon/JSON/projects.json", "w") as dest:
        json.dump(obj, dest, indent=4)

#send()
delete(input())