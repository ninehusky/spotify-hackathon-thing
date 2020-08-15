from flask import Flask
app = Flask(__name__)
# mybranch version :)

@app.route('/')
def hello_world():
    return 'Hello, world'