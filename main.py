from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
  return render_template('signup.html')

def validcredentials(user_entry):
  if len(user_entry) < 3 or len(user_entry) > 20:
    return False
  
  for i in user_entry:
    if i == ' ':
      return False
    else:
      return True

def samepass(password,verified):
  if password == verified:
    return True
  else:
    return False

def emailcheck(email):
  if len(email) == 0:
    return True
  for i in email:
    if i == ' ':
      return False
  if len(email) <= 3 or len(email) > 20:
    return False
  elif email.count("@") > 1:
    return False
  elif email.count(".") > 1:
    return False
  else:
    return True


@app.route("/welcome", methods=["POST"])
def validate():
  username = request.form['username']
  password = request.form['password']
  verified = request.form['verified']
  email = request.form['email']

  user_error = ''
  password_error = ''
  verified_error = ''
  email_error = ''

  if validcredentials(username) == False:
    user_error = "That's not a valid Username."
    

  if validcredentials(password) == False:
    password_error = "That's not a valid Password."
    password = ''
  
  if samepass(password,verified) == False:
    verified_error = "Passwords don't match."
    verified = ''

  if emailcheck(email) == False:
    email_error = "That's not a valid Email Address."
    
  
  if not user_error and not password_error and not verified_error and not email_error:
    return render_template('welcome.html', username=username)
  else:
    return render_template('signup.html', user_error = user_error, password_error= password_error, verified_error = verified_error, email_error = email_error, username=username,password=password,verified=verified,email=email )
  


app.run()

