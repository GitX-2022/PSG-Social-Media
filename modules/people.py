import json
import datetime

def send():
    with open ("Hackathon/JSON/people.json","r") as source:
        obj = json.load(source)
    
    Roll_No = str(input())
    data = {
    "People": [
    {
        "Roll_No.": Roll_No,
        "First Name": str(input()),
        "Last Name" : str(input()),
        "Location": str(input()),
        "Thumbnail": str(input()),
        "About": str(input()),
        "Education": [
            {
                "School": [
                    {
                        "Name": str(input()),
                        "Start Date": str(datetime.datetime.now())[:-7],
                        "End Date": str(datetime.datetime.now())[:-7],
                        "Location": str(input()),
                        "Description": str(input()),
                        "Logo": str(input()),
                        "Link": str(input())
                    }
                ],
                "PSG College Of Technology": [
                    {
                        "Course": str(input()),
                        "Start Date": str(datetime.datetime.now())[:-7],
                        "End Date": str(datetime.datetime.now())[:-7],
                        "Course Topic": str(input()),
                        "Class": str(input())
                    }
                ]
            }
        ]
    },
    {
        "Courses and Co-Curricular Experiences (Cerificates, Internships)": [
            {
                "Title": str(input()),
                "Organization": str(input()),
                "Start Date": str(datetime.datetime.now())[:-7],
                "End Date": str(datetime.datetime.now())[:-7],
                "Field": str(input()),
                "Description": str(input()),
                "Logo": str(input()),
                "Link": str(input())

            },
            {
                "Title": str(input()),
                "Organization": str(input()),
                "Start Date": str(datetime.datetime.now())[:-7],
                "End Date": str(datetime.datetime.now())[:-7],
                "Field": str(input()),
                "Description": str(input()),
                "Logo": str(input()),
                "Link": str(input())

            }
        ]
    },
    {
        "Scores:": [
            {
                "Grade 10": [
                    {
                        "Title": str(input()),
                        "Score": str(input()),
                        "Logo": str(input())
                    }
                ],
                "Grade 12": [
                    {
                        "Title": str(input()),
                        "Score": str(input()),
                        "Logo": str(input())
                    }
                ]
            }
        ]
    },
    {
        "Languages":[
            {
                "Name": str(input()),
                "Proficiency" : str(input())
            }
        ]
    },
    {
        "Login Details":[
            {
                "List of IPs": str(input()),
                "List of ":[
                    {
                        "City": str(input()),
                        "Country": str(input())
                    }
                ]
            }
        ]
    },
    {
        "Posts":[
            {
                "Timestamp": str(datetime.datetime.now()),
                "HTML Content": str(input()),
                "Likes": [
                    {
                        "By MemberID": str(input()),
                        "Timestamp": str(input())
                    }
                ],
                "Comment": [
                    {
                        "By MemberID": str(input()),
                        "Timestamp": str(datetime.datetime.now()),
                        "ID": str(input()),
                        "Text": str(input())
                    }
                ]
            },
            {
                "Timestamp": str(datetime.datetime.now()),
                "HTML Content": str(input()),
                "Likes": [
                    {
                        "By MemberID": str(input()),
                        "Timestamp": str(datetime.datetime.now())
                    }
                ],
                "Comment": [
                    {
                        "By MemberID": str(input()),
                        "Timestamp": str(datetime.datetime.now()),
                        "ID": str(input()),
                        "Text": str(input())
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

#send()
delete(input())