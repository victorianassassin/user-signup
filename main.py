from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True



@app.route("/signup", methods=['POST'])
def signup():

    error_username = ""
    error_passwords = ""
    error_verifypasswords = ""
    error_email = ""

    username = request.form['username']
    passwords = request.form['passwords']
    verifypasswords = request.form['verifypasswords']
    email = request.form['email']
    
    if len(username) < 3 or len(username) > 20 or " " in username:
        error_username = " That's not a valid username"
        

    if len(passwords) < 3 or len(passwords) > 20 or " " in passwords:
        error_passwords = " That's not a valid passwords"
      

    if not passwords == verifypasswords:
        error_verifypasswords = " Passwords don't match"
        

    if  not email=="":
        
        
        if len(email) < 3 or len(email) > 20 or " " in email or not ("." in email or "@" in email):
            error_email = " That's not a valid email"
    
   
     

    # check if error_var is empty string then go to confirmation page        
    if  not error_username and not error_passwords and not error_verifypasswords and not error_email:
         return render_template('confirmation.html', username=username)
    
    else:
       
        
        return render_template('edit.html',username=username, email=email, error_username=error_username, error_passwords=error_passwords, error_verifypasswords=error_verifypasswords, error_email=error_email)
            


@app.route("/")
def index():
    return render_template('edit.html')

app.run()

