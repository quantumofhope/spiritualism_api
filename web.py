from flask import Flask
app=Flask(__name__)


@app.route('/')
def index():
  return "Hello Staging!!"

@app.route('/api/<username>')
def show_user_profile(username):
    # show the user profile for that user
    resp = f'User = {username}'
    return resp

@app.route('/about')
def about():
  return "What about this then!!"
