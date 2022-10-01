from flask import *
import json
import modules.editor as editor
import modules.events as events
import modules.people as people
import modules.roombooking as rooms

app = Flask(__name__)
app.secret_key = "KrrrzPPghtfgSKbtJEQCTA"
app.PROPAGATE_EXCEPTIONS = True

@app.route('/')
def rerouter():
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    return redirect(url_for("dashboard"))

@app.route('/login', methods=['POST','GET'])
def login_page():
    if request.method=='GET':
        return render_template("login.htm", incorrect = "false")
    elif request.method=='POST':
        try:
            ip=dict(request.headers)['X-Forwarded-For']
        except:
            ip=dict(request.headers).get('X-Real-Ip')
        rollno = request.form.get("rollno")
        passwd = request.form.get("password")
        if people.authUser(rollno,passwd).get("auth")==True:
            session["login"] = json.dumps({"login":True,
                                        "name":(people.authUser(rollno,passwd).get("user").get("First Name")+people.authUser(rollno,passwd).get("user").get("Last Name")),
                                        "roll":people.authUser(rollno,passwd).get("Roll No.")}) # and login details
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.htm", incorrect = "true")


@app.route('/sign-up', methods=['POST','GET'])
def signup_page():
    if request.method=='GET':
        return render_template("sign_up/sign_up.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.htm",
                            name = json.loads(session.get("login"))["name"],
                            events=[
                                    {
                                        "event_name" : "GitX",
                                        "event_details" : "Code Hawk Official"
                                    }
                                   ])


@app.route('/my-profile')
def my_profile():
    return render_template("profile.html",
                            person={
                                    "roll_no": "21Z202",
                                    "name"   : "Aaditya",
                                    "dept"   : "CSE",
                                    "coding_languages" : ["Python", "HTML"]
                                },
                            recent_cert={"image":"https://ecdn.teacherspayteachers.com/thumbitem/-RAK-Random-Acts-of-Kindness-EDITABLE-Certificates-5243375-1583679292/original-5243375-1.jpg",
                                         "title":"Kind Person",
                                         "details":"Random act of Kindness Certificate"})

@app.route('/events')
def events():
    return render_template("events.html",
                            events = [
                                        {
                                            "logo" : "",
                                            "title": "GitX",
                                            "desc" : "GitHub Campus Club Hackathon"
                                        },
                                        {
                                            "logo" : "",
                                            "title": "What's Hackening?",
                                            "desc" : "Ethical Hacking Hackathon"
                                        }
                                     ])

@app.route('/rooms')
def rooms():
    with open(f"data/rooms.json") as f:
        rooms = json.load(f)
    return render_template("admin/view_room.htm",
                            rooms = rooms.get("rooms"))

@app.route('/rooms/delete/<code>@<dt>')
def delete_booking(code,dt):
    with open(f"data/rooms.json") as f:
        rooms = json.load(f)
    return render_template("admin/view_room.htm",
                            rooms = rooms.get("rooms"))

@app.route('/rooms/update/<code>@<dt>')
def update_booking(code,dt):
    with open(f"data/rooms.json") as f:
        rooms = json.load(f)
    return render_template("admin/view_room.htm",
                            rooms = rooms.get("rooms"))

@app.route('/chats')
def chats():
    with open(f"data/chats.json") as f:
        chats = json.load(f)
    user_chats = []
    for i in chats.get("chat_logs"):
        if (json.loads(session.get("login")).get("roll").upper()==i.get("sender_ID").upper()):
            if i.get("receiver_ID").upper() not in user_chats:
                if i.get("receiver_ID")!=json.loads(session.get("login")).get("roll").upper():
                    print(user_chats)
                    user_chats.append(i.get("receiver_ID").upper())
        if (json.loads(session.get("login")).get("roll").upper()==i.get("receiver_ID").upper()):
            if i.get("sender_ID").upper() not in user_chats:
                if i.get("sender_ID")!=json.loads(session.get("login")).get("roll").upper():
                    print(user_chats)
                    user_chats.append(i.get("sender_ID").upper())
    return render_template("chat_main.html", user_chats = user_chats)

@app.route('/chats/<roll>')
def chat_roll(roll):
    with open(f"data/chats.json") as f:
        chats = json.load(f)
    my_chats = []
    for i in chats.get("chat_logs"):
        if (i.get("receiver_ID")==roll) or (i.get("sender_ID")==roll):
            my_chats.append(i)
    return render_template("chat_ui.html", my_chats = my_chats, person=roll)

@app.route('/chats/unsend/<id>')
def delete_chat(id):
    pass

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("rerouter"))

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=56789)