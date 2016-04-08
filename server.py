import requests
import logging

from flask import Flask, request, Response, render_template, make_response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!\n"

@app.route("/svzyw0hb.htm")
def verify():
    return render_template('svzyw0hb.htm')

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
    url = request.form['url']
    print url
    page = requests.get(url)
    print page.content
    resp = make_response(page.content)
    return resp


if __name__ == "__main__":
    context = ('proxy.crt', 'proxy.key')
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True, debug=True)