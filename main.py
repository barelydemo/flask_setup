from flask import Flask, request, redirect, Response, url_for, session

app = Flask(__name__)
app.secret_key = "SuperSecret" #must for session in order to secure our session

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username") #reading the data
        password = request.form.get("password")

        if username == "admin" and password == "abc1":
            session["user"] = username #store in session
            return redirect(url_for("welcome"))
        
        else:
            return Response("In-valid credentials. Try again.", mimetype="text/plain")
            
            #what kind of content you wanna return. by default html type

    return '''
            <h2>LOGIN PAGE</h2>
            <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="text" name="password"><br>
            <input type="submit" value="Login">
            </form>
            '''

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2>Welcome, {session["user"]}!</h2>
            <a href={url_for('logout')}>Logout</a>
        '''
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None) #if user is not in session, handles errors.
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
