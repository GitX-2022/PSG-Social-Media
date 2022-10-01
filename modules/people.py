import json
import datetime

def addUser(Roll_No, First_Name, Last_Name, Location, Thumbnail, About, Passwd, C_Title, C_Organization, C_Start_Date, C_End_Date, C_Field, C_Description, C_Logo, C_Link, L_Name, L_Proficiency, List_IP, L_City, L_Country):
    with open ("Hackathon/JSON/people.json","r") as source:
        obj = json.load(source)
    
    data = {
    "People": [
    {
        "Roll_No.": Roll_No,
        "First Name": First_Name,
        "Last Name" : Last_Name,
        "Location": Location,
        "Thumbnail": Thumbnail,
        "About": About,
        "Passwd": Passwd,
    },
    {
        "Courses and Co-Curricular Experiences (Cerificates, Internships)": [
            {
                "Title": C_Title,
                "Organization": C_Organizaiton,
                "Start Date": C_Start_Date,
                "End Date": C_End_Date,
                "Field": C_Field,
                "Description": C_Description,
                "Logo": C_Logo,
                "Link": C_Link

            }
        ]
    },
    {
        "Languages":[
            {
                "Name": L_Name,
                "Proficiency" : L_Proficiency
            }
        ]
    },
    {
        "Login Details":[
            {
                "List of IPs": List_IP,
                "List of ":[
                    {
                        "City": L_City,
                        "Country": L_Country
                    }
                ]
            }
        ]
    }
]
}
    obj["People"].append(data)

    with open("Hackathon/JSON/people.json","w") as dest:
        json.dump(obj, dest, indent=4)
    
def read():
    with open("Hackathon/JSON/people.json","r") as source:
        obj = json.load(source)
    for i in (obj["People"]):
        print(i)

def delete(Roll_No):
    with open ("Hackathon/JSON/people.json", "r") as source:
        obj = json.load(source)
    if (obj["People"][0]["Roll_No."] == Roll_No):
        obj["Groups"].remove(i)
    
    for i in obj["People"]:
        print(i)
    with open("Hackathon/JSON/people.json", "w") as dest:
        json.dump(obj, dest, indent=4)
