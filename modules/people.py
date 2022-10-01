''' This code is Open Source Code for the GitX GitHub x PSG Tech Hackathon 2022.
    Team CodeHawk
    - Aaditya Rengarajan
    - Ajay Ramesh
    - S Karun Vikhash
    - Sanjay Kumaar Easwaran '''

import json
import datetime

def addUser(roll_no:str,
            fname:str,
            lname:str,
            passwd:str,
            languages:list,
            ip:str):

    with open ("data/people.json","r") as source:
        obj = json.load(source)
    
    data =  {
              "Roll No.": roll_no,
              "First Name": fname,
              "Last Name": lname,
              "Passwd": passwd,
              "Languages": languages,
              "Login Details": [
                {
                  "List of IPs": [
                    ip
                  ]
                }
              ]
            }

    obj["people"].append(data)

    with open("data/people.json","w") as dest:
        json.dump(obj, dest, indent=4)
    
def read():
    with open("data/people.json","r") as source:
        obj = json.load(source)
    return obj

def authUser(user:str,
             password:str):

    with open("data/people.json","r") as source:
        obj = json.load(source)

    for i in obj["people"]:
        if i["Roll No."]==user:
            if i["Passwd"]==password:
                return {"auth":True,"user":i}
    return {"auth":False}

def chgPwd(user:str,
             password:str):

    with open("data/people.json","r") as source:
        obj = json.load(source)

    for i in obj["people"]:
        if i["Roll No."]==user:
            i["Passwd"] = password

    with open("data/people.json","w") as dest:
        json.dump(obj, dest, indent=4)