   if len(username)< 3 or len(username) > 20:
        error = " That's not a valid username" 

        return redirect("/?error=" + error)

    if len(password)  < 3 or len(password) > 20:
        error = " That's not a valid password" 

        return render_template('edit.html', error=error)

    if not password == verifypassword:
        error = " Passwords dont match" 
        return render_template('edit.html', error=error)

    if "." and "@" not in email:
        error = " That's not a valid email"

        return redirect("/?error=" + error)