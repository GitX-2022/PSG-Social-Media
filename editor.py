import json
import datetime
import emoji



def send():
    '''
    Sending the message and logging it to chats.json
    '''

    sender_id = input()
    receiver_id = input()
    message = str(input())
    emoji = input()

    data = {"sender_ID": sender_id , "receiver_ID":receiver_id ,"timestamp": str(datetime.datetime.now())[:-7], "message": message, "emoji": emoji, "reaction": ""}
    print(data)
    with open("chats.json", "a") as dest:
        dest.write(",\n")
        json.dump(data, dest, indent=4)


def update():
    '''
    Updating if the user gives any reactions
    '''
    with open("chats.json", "r") as source:
        obj = json.load(source)
    print(obj)

#send()
update()