from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    passwords = request.form['passwords']
    verifypasswords = request.form['verifypasswords']
    email = request.form['email']


    # Need to make if statement goes thru whole 4 conditino instead of return when one first condition meets.
    
    if len(username) < 3 or len(username) > 20 or " " in username:
        #error = " That's not a valid username"

        #return render_template('edit.html', error=error)
        print ("That's not a valid username")
    if len(passwords) < 3 or len(passwords) > 20 or " " in passwords:
        error_passwords = " That's not a valid passwords"

        return render_template('edit.html', error_passwords=error_passwords)

    if not passwords == verifypasswords:
        error_verifypasswords = " Passwords don't match"

        return render_template('edit.html', error_verifypasswords=error_verifypasswords)

    if len(email) < 3 or len(email) > 20 or " " in email and not ("." in email or "@" in email):
        error_email = " That's not a valid email"
        
        return render_template('edit.html', error_email=error_email)

    return render_template('confirmation.html', username=username)



@app.route("/")
def index():
    return render_template('edit.html')

app.run()

