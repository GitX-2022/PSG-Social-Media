import json
import datetime

def send(Title, Description, Url, Thumbnail, Languages, Vaccancies, Members, M_Name, M_Date, M_Description_1, Me_Name, Me_Roll):
    with open ("Hackathon/JSON/projects.json","r") as source:
        obj = json.load(source)
    
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
