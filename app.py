from flask import Flask

import os

app = Flask(__name__)

@app.route('/')
def hello():
    print(app.instance_path)
    return os.path.join(app.instance_path, 'test') #C:\Users\RajanD\OneDrive - AMI\Desktop\flaskProject\instance\test