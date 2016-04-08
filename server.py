import requests

from flask import Flask, request, Response, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!\n"


@app.route("/test")
def areyouaproxy():
    if "X-Forwarded-For" in request.headers:
        return "Yes, You are behind a proxy\n"
    else:
        return "I didn't see any evidence of a proxy\n"


@app.route("/proxy", methods=['GET','POST'])
def proxy():
    return render_template('proxy.html')

# fetch a web page and render it
@app.route("/fetch", methods=['POST'])
def fetch():
    url = request.args.get('key', '')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)