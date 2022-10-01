import json
import datetime

'''
This code is Open Source Code for the GitX GitHub x PSG Tech Hackathon 2022.
	Team CodeHawk
	- Aaditya Rengarajan
	- Ajay Ramesh
	- S Karun Vikhash
	- Sanjay Kumaar Easwaran
'''


def send(sender_id:int, reciever_id:int, message:str):
    '''
    Inputs(4):
        sender_id(int): Unique identifier for the sender/user
        reciever_id(int): Unique identifier for the receiver
        message(string): Actual message content
    
    Output:
        Data is logged into the json file
    '''
    
    with open("chats.json", "r") as source:
        obj = json.load(source)

    data = {"text_id": str(int(obj["chat_logs"][-1]["text_id"]) + 1),"sender_ID": sender_id , "receiver_ID":receiver_id ,"timestamp": str(datetime.datetime.now())[:-7], "message": message, "emoji": "obslete", "reaction": ""}
    obj["chat_logs"].append(data)

    with open("chats.json", "w") as dest:
        json.dump(obj, dest, indent=4)


def update(text_id:int, sender_id:int, receiver_id:int):
    '''
    Updating if the user gives any reactions in chats.json
    Parameters :(text_id, sender_id, receiver_id)
    '''

    with open("chats.json", "r") as source:
        obj = json.load(source)
    for i in (obj["chat_logs"]):
        if(i["text_id"] == text_id and i["sender_ID"] == sender_id and i["receiver_ID"] == receiver_id):
            i["reaction"] = input()

    with open("chats.json", "w") as dest:
        json.dump(obj, dest, indent=4)


def read():
    '''
    Display the contents of the json file
    '''
    with open("chats.json", "r") as source:
        obj = json.load(source)
    for i in (obj["chat_logs"]):
        print(i)


def delete(text_id, sender_id, receiver_id):
    '''
    To delete chats which were sent unintentionally
    Parameters :(text_id, sender_id, receiver_id)
    '''
    with open("chats.json", "r") as source:
        obj = json.load(source)
    for i in obj["chat_logs"]:
        if(i["text_id"] == text_id and i["sender_ID"] == sender_id and i["receiver_ID"] == receiver_id):
            obj["chat_logs"].remove(i)

    for i in obj["chat_logs"]:
        print(i)
    with open("chats.json", "w") as dest:
        json.dump(obj, dest, indent=4)


#send()
#update(input(), input(), input())
#read()
#delete(input(), input(), input())
