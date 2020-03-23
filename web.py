from flask import Flask

app = Flask(__name__)

@app.route('/hello')

def helloIndex():
    return 'Hello World from Python Flask!'

@app.route('/welcome')
def welcomeIndex():
    return 'Welcome to the local web host!'

app.run(host='0.0.0.0', port=5000)