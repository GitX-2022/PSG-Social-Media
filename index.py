''' This code is Open Source Code for the GitX GitHub x PSG Tech Hackathon 2022.
    Team CodeHawk
    - Aaditya Rengarajan
    - Ajay Ramesh
    - S Karun Vikhash
    - Sanjay Kumaar Easwaran '''

from flask import *
import json, uuid
from datetime import datetime

import modules.editor as editor
import modules.events as eventseditor
import modules.people as people
import modules.roombooking as roomseditor
import modules.mailer_hasher as mail
from modules.certgen import certgen
from modules.certgen import ticktgen

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
        rollno = request.form.get("rollno")
        passwd = mail.get_hash(request.form.get("password"))
        if people.authUser(rollno,passwd).get("auth")==True:
            session["login"] = json.dumps({"login":True,
                                        "name":(people.authUser(rollno,passwd).get("user").get("First Name")+" "+people.authUser(rollno,passwd).get("user").get("Last Name")),
                                        "roll":people.authUser(rollno,passwd).get("user").get("Roll No."),
                                        "details":people.authUser(rollno,passwd).get("user")})
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.htm", incorrect = "true")


@app.route('/sign-up', methods=['POST','GET'])
def signup_page():
    if request.method=='GET':
        return render_template("sign_up/sign_up.html")
    if request.method=='POST':
        if session.get("OTP"):
            if session.get("OTP")==request.form.get("OTP"):
                try:
                    ip=dict(request.headers)['X-Forwarded-For']
                except:
                    ip=dict(request.headers).get('X-Real-Ip')
                people.addUser(json.loads(session.get("signUpForm")).get("rollno"),
                                json.loads(session.get("signUpForm")).get("fname"),
                                json.loads(session.get("signUpForm")).get("lname"),
                                json.loads(mail.get_hash(session.get("signUpForm")).get("user_password")),
                                ", ".split(request.form.get("languages")),
                                ip)
                rollno = json.loads(session.get("signUpForm")).get("rollno")
                passwd = json.loads(mail.get_hash(session.get("signUpForm")).get("user_password"))
                session.clear()
                session["login"] = json.dumps({"login":True,
                                           "name":(people.authUser(rollno,passwd).get("user").get("First Name")+" "+people.authUser(rollno,passwd).get("user").get("Last Name")),
                                           "roll":people.authUser(rollno,passwd).get("user").get("Roll No."),
                                           "details":people.authUser(rollno,passwd).get("user")})
                return redirect(url_for("dashboard"))
            else:
                return json.dumps(['invalid OTP',session.get("OTP"),request.form.get("OTP"),session.get("OTP")==request.form.get("OTP")], indent=4)
        else:
            session["OTP"] = str(uuid.uuid4()).split("-")[0].upper()
            mail.send(str(request.form.get("rollno")+"@psgtech.ac.in"),"Your OTP for Eventique",session.get("OTP"))
            session["signUpForm"] = json.dumps(dict(request.form))
            return render_template("sign_up/confirm_ip.htm")

@app.route('/forgot-password', methods=['POST','GET'])
def forgot_pass():
    if request.method=='GET':
        session["OTP"] = str(uuid.uuid4()).split("-")[0].upper()
        mail.send(str(dict(request.args).get("rollno")+"@psgtech.ac.in"),"Your OTP for Eventique",session.get("OTP"))
        session["rollno"] = (str(dict(request.args).get("rollno")))
        return render_template("forgot_pass/retrieve_otp.htm")
    if request.method=='POST':
        if session.get("OTP"):
            if session.get("OTP")==request.form.get("OTP"):
                try:
                    ip=dict(request.headers)['X-Forwarded-For']
                except:
                    ip=dict(request.headers).get('X-Real-Ip')
                people.chgPwd(session.get("rollno"), mail.get_hash(request.form.get("pwd")))
                rollno = session.get("rollno")
                passwd = mail.get_hash(request.form.get("pwd"))
                session.clear()
                session["login"] = json.dumps({"login":True,
                                           "name":(people.authUser(rollno,passwd).get("user").get("First Name")+" "+people.authUser(rollno,passwd).get("user").get("Last Name")),
                                           "roll":people.authUser(rollno,passwd).get("user").get("Roll No."),
                                           "details":people.authUser(rollno,passwd).get("user")})
                return redirect(url_for("dashboard"))
            else:
                return json.dumps(['invalid OTP',session.get("OTP"),request.form.get("OTP"),session.get("OTP")==request.form.get("OTP")], indent=4)

@app.route('/dashboard')
def dashboard():
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    return render_template("dashboard.htm",
                            name = json.loads(session.get("login"))["name"],
                            events=eventseditor.userEvents(json.loads(session.get("login"))["roll"]))


@app.route('/my-profile')
def my_profile():
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    print(json.loads(session.get("login"))["details"])
    return render_template("profile.html",
                            person=json.loads(session.get("login"))["details"],
                            recent_cert={"image":"https://ecdn.teacherspayteachers.com/thumbitem/-RAK-Random-Acts-of-Kindness-EDITABLE-Certificates-5243375-1583679292/original-5243375-1.jpg",
                                         "title":"Kind Person",
                                         "details":"Random act of Kindness Certificate"})

@app.route('/events')
def events():
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    if request.args.get("enroll"):
        eventseditor.attendEvent(json.loads(session.get("login"))["roll"], request.args.get("enroll"))
    return render_template("events.html",
                            events = eventseditor.read(),
                            me = json.loads(session.get("login"))["roll"])

@app.route('/ticket/<event>', methods=['POST','GET'])
def ticket(event):
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    ticktgen.tgen(eventseditor.getEvent(event)["Organizer's Name"],
                  json.loads(session.get("login"))["roll"],
                  eventseditor.getEvent(event)["Start Date"],
                  eventseditor.getEvent(event)["End Date"],
                  eventseditor.getEvent(event)["Event Name"])
    return send_file("tickettt.png")

@app.route('/rooms')
def rooms():
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    return render_template("admin/view_room.htm",
                            rooms = roomseditor.viewbookings(),
                            me = json.loads(session.get("login"))["roll"])

@app.route('/rooms/delete/<code>@<dt>')
def delete_booking(code,dt):
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    with open(f"data/rooms.json") as f:
        rooms = json.load(f)
    return render_template("admin/view_room.htm",
                            rooms = rooms.get("rooms"))

@app.route('/rooms/update/<code>@<dt>')
def update_booking(code,dt):
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    with open(f"data/rooms.json") as f:
        rooms = json.load(f)
    return render_template("admin/view_room.htm",
                            rooms = rooms.get("rooms"))

@app.route('/profile-settings')
def settings():
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    return render_template("profile_settings.html",
                            me = json.loads(session.get("login"))["roll"],
                            admin = json.loads(session.get("login")).get("details").get("admin"))

@app.route('/book-room', methods=['POST','GET'])
def book_room():
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    if request.method=='GET':
        return render_template("admin/book_room.htm")
    if request.method=='POST':
        rn = request.form.get("room")
        dt = request.form.get("dt")
        p = request.form.get("p")
        by = json.loads(session.get("login"))["roll"]
        roomseditor.addbooking(rn,dt,p,by)
        return redirect(url_for('rooms'))

@app.route('/add-event', methods=['POST', 'GET'])
def add_event():
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    if request.method=='GET':
        return render_template("admin/update_event.htm")
    if request.method=='POST':
        eventseditor.add(request.form.get("eve_name"),
                         request.form.get("start_date"),
                         request.form.get("end_date"),
                         request.form.get("sem_open"),
                         request.form.get("dep_open"),
                         request.form.get("or_name"),
                         request.form.get("desc"))
        return redirect(url_for("events"))

@app.route('/chats')
def chats():
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    with open(f"data/chats.json") as f:
        chats = json.load(f)
    user_chats = []
    for i in chats.get("chat_logs"):
        if (json.loads(session.get("login")).get("roll").upper()==i.get("sender_ID").upper()):
            if i.get("reciever_ID").upper() not in user_chats:
                if i.get("reciever_ID")!=json.loads(session.get("login")).get("roll").upper():
                    print(user_chats)
                    user_chats.append(i.get("reciever_ID").upper())
        if (json.loads(session.get("login")).get("roll").upper()==i.get("reciever_ID").upper()):
            if i.get("sender_ID").upper() not in user_chats:
                if i.get("sender_ID")!=json.loads(session.get("login")).get("roll").upper():
                    print(user_chats)
                    user_chats.append(i.get("sender_ID").upper())
    return render_template("chat_main.html", user_chats = user_chats)

@app.route('/chats/<roll>')
def chat_roll(roll):
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    with open(f"data/chats.json") as f:
        chats = json.load(f)
    my_chats = []
    print(chats)
    for i in chats.get("chat_logs"):
        if (i.get("reciever_ID").upper()==roll.upper()) or (i.get("sender_ID").upper()==roll.upper()):
            my_chats.append(i)
    return render_template("chat_ui.html", my_chats = my_chats, person=roll,
                            me = json.loads(session.get("login"))["roll"])

@app.route('/chats/send/<id>', methods=['POST', 'GET'])
def send_chat(id):
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    to = id
    message = request.form.get("message")
    fro = json.loads(session.get("login"))["roll"]
    editor.send(fro, to, message)
    return redirect(url_for("chat_roll", roll=to))

@app.route('/chats/unsend/<id>', methods=['POST', 'GET'])
def delete_chat(id):
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    editor.delete(id)
    return redirect(url_for("chat_roll", roll=request.args.get("callback")))

@app.route('/generate-certificate', methods=['POST','GET'])
def gen_cert():
    if session.get("login") == None:
        return redirect(url_for("login_page"))
    if request.method=='GET':
        return render_template("admin/gen_cert.htm")
    if request.method=='POST':
        rn = request.form.get("clubname")
        nm = request.form.get("name")
        dt = datetime.now().strftime("%d/%m/%Y")
        request.files['logo'].save("logo.png")
        p = "logo.png"
        certgen.cgen(rn,nm,dt,p)
        return send_file("certificate.png")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("rerouter"))


''' API to
    - Retrieve booked rooms
    - Retrieve my events (Requires Log-In)
    - Retrieve event ticket given event ID'''

@app.route('/api/rooms')
def rooms_api():
    return jsonify(roomseditor.viewbookings())

@app.route('/api/login', methods=['POST','GET'])
def api_login():
    rollno = request.form.get("rollno")
    passwd = request.form.get("password")
    if people.authUser(rollno,passwd).get("auth")==True:
        session["login"] = json.dumps({"login":True,
                                    "name":(people.authUser(rollno,passwd).get("user").get("First Name")+" "+people.authUser(rollno,passwd).get("user").get("Last Name")),
                                    "roll":people.authUser(rollno,passwd).get("user").get("Roll No."),
                                    "details":people.authUser(rollno,passwd).get("user")})
        return jsonify({"message":"login successful"})
    else:
        return jsonify({"message":"incorrect login"})

@app.route('/api/events')
def events_api():
    return jsonify(eventseditor.userEvents(json.loads(session.get("login"))["roll"]))

@app.route('/api/ticket/<event>', methods=['POST','GET'])
def api_ticket(event):
    ticktgen.tgen(eventseditor.getEvent(event)["Organizer's Name"],
                  json.loads(session.get("login"))["roll"],
                  eventseditor.getEvent(event)["Start Date"],
                  eventseditor.getEvent(event)["End Date"],
                  eventseditor.getEvent(event)["Event Name"])
    return send_file("tickettt.png")

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=56789)