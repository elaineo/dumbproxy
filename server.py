import requests

from flask import Flask, request, Response, render_template, make_response
from werkzeug.datastructures import Headers

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
    try:
        h = Headers(request.headers)
        h.clear()
        h.add('referer', 'https://www.facebook.com/')

        r = requests.request(
            method='GET',
            url=url,
            headers=h,
            timeout=5
        )
    except (
            requests.exceptions.Timeout,
            requests.exceptions.ConnectTimeout,
            requests.exceptions.ReadTimeout):
        return Response(status=504)
    except (
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.TooManyRedirects):
        return Response(status=502)
    except (
            requests.exceptions.RequestException,
            Exception) as e:
        if app.debug:
            raise e
        return Response(status=500)

    mimetype = "text/html"
    return Response(r.content, mimetype=mimetype)



if __name__ == "__main__":
    context = ('proxy.crt', 'proxy.key')
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True, debug=True)