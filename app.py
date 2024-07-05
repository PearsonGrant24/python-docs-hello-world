from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! Pear. We want an example of speach sythnesys in Englich and SHona"
    
