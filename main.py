from flask import Flask
app=Flash(__name__)

@app.route('/')
def hello():
  return "Hello World,This is Chandra Sekhar :-)"
    
