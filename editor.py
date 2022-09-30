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

    data = {"text_id": int(obj["chat_logs"][-1]["text_id"]) + 1,"sender_ID": sender_id , "receiver_ID":receiver_id ,"timestamp": str(datetime.datetime.now())[:-7], "message": message, "emoji": emoji, "reaction": ""}
    obj["chat_logs"].append(data)

    with open("chats.json", "w") as dest:
        json.dump(obj, dest, indent=4)


def update(text_id, sender_id, receiver_id):
    '''
    Updating if the user gives any reactions
    '''

    with open("chats.json", "r") as source:
        obj = json.load(source)
    for i in (obj["chat_logs"]):
        print(i)


#send()
update()
