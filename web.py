from flask import Flask, jsonify
app=Flask(__name__)


@app.route('/')
def index():
  return "Hello World!!"
  
@app.route('/api')
def api():
  return jsonify({"status":"ok", "payload":("name":"John", "place":"Bournemouth"})
  
