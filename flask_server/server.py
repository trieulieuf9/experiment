from flask import Flask
from flask import Response
from flask import request
from flask import render_template
from os import listdir
from os import path

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


# Content-Type: text/plain; charset=UTF-8

# listing all available webhooks
@app.route('/webhooks')
def webhooks():
    response = ""
    for filename in listdir("webhook_templates"):
        response += '<a href="/webhook/{}">{}</a><br><br>'.format(filename, filename)

    return response


# response with headers and body specified in requested filename
@app.route('/webhook/<filename>')
def webhook_response(filename):
    file_path = path.join("webhook_templates", filename)
    response = Response()
    read_header = False
    read_body = False
    body = ""
    with open(file_path) as webhook_template:
        for line in webhook_template:
            line_stripped = line.strip()
            if line_stripped == "--- HEADER ---":
                read_header = True
                continue
            elif line_stripped == "--- BODY ---":
                read_header = False
                read_body = True
                continue

            if read_header and line_stripped != "":
                header = line_stripped.split(":")
                response.headers[header[0]] = header[1]

            if read_body:
                body += line

    print("HELLO: ", body)

    response.set_data(body)
    return response


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

