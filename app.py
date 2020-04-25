from flask import Flask, render_template, url_for, jsonify
from getInfo import GetDialogue

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/getHelp')
def getHelp():
    data = GetDialogue()
    dialogue = data.getDialogue()
    result = {'dialogue': dialogue}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)