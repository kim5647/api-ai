from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/pisun", methods=['Get'])
def pisun():
    print("you pidor")
    return "Hello, World!"

@app.route("/kirill/pidor", methods=['POST'])
def kirill():
    if request.method == 'POST':
        name = request.json['name']
        nickname = request.json['nickname']
        print(name + " pidor and " + nickname)
        return name + " pidor and " + nickname


app.run(port=8080, debug=True)