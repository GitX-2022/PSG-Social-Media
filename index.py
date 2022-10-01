from flask import *
import json

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
        return render_template("login.htm")
    elif request.method=='POST':
        rollno = request.form.get("rollno")
        passwd = request.form.get("password")
        # VERIFY PASSWORD
        session["login"] = json.dumps({"login":True,
                                        "name":"Aaditya"}) # and login details
        return redirect(url_for("dashboard"))

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

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("rerouter"))

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=56789)