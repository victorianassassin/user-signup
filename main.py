from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route ("/welcome", methods=['POST'])

def username():
    username = request.form['username']
   #username_escaped = cgi.escape(username, quote=True)
    password = request.form['password']

    email = request.form['email']

    if len(username)< 3 or len(username) > 20:
        error = " That's not a valid username" 

        return print(error) 

    if len(password)==0 or password < 3 or password > 20:
        error = " That's not a valid password" 

        return redirect("/?error=" + error)
    if "." and "@" not in email:
        error = " That's not a valid email"

        return redirect("/?error=" + error)
    
    return render_template('confirmation.html', username=username)

@app.route("/")
def index():
    return render_template('edit.html')
 
app.run()