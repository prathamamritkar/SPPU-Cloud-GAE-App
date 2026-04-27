import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h1>SPPU Cloud Computing Assignment</h1>
    <p><b>Name:</b> Pratham Amritkar</p>
    <p><b>Roll No:</b> 23CO009</p>
    <p><b>Status:</b> Successfully Deployed on Google App Engine!</p>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
