from flask import Flask, send_from_directory, request, render_template, render_template_string, jsonify, make_response
app = Flask(__name__)


@app.route('/')
def index():
	# response = make_response("whatever")
	# response.status = 101
    return "", 101


@app.route('/cors')
def cors():
	response = make_response("whatever")
	response.headers["Access-Control-Allow-Origin"] = "*"
	response.headers["access-control-allow-headers"] = "Random-Header"
	response.headers["access-control-expose-headers"] = "*"
	response.headers["Pragma"] = "dude"
	response.headers["Random-Header"] = "hello world"
	return response


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000, debug=True)