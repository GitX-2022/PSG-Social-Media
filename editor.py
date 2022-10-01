import json
import datetime



def send():
    '''
    Sending the message and logging it to chats.json
    '''

    sender_id = input()
    receiver_id = input()
    message = str(input())
    emoji = input()
    
    with open("chats.json", "r") as source:
        obj = json.load(source)

    data = {"text_id": str(int(obj["chat_logs"][-1]["text_id"]) + 1),"sender_ID": sender_id , "receiver_ID":receiver_id ,"timestamp": str(datetime.datetime.now())[:-7], "message": message, "emoji": emoji, "reaction": ""}
    obj["chat_logs"].append(data)

    with open("chats.json", "w") as dest:
        json.dump(obj, dest, indent=4)


def update(text_id, sender_id, receiver_id):
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
