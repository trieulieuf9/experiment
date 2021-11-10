from flask import Flask, send_from_directory, request, render_template, render_template_string, jsonify, make_response, request
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!!!\n', 200


@app.route('/set-cookie')
def set_cookie():
	resp = make_response("cookies are set")
	resp.set_cookie("samesite_none", "dude1", samesite="None", domain="trieulieuf9.com", secure=True)
	resp.set_cookie("samesite_lax", "dude2", samesite="Lax", domain="trieulieuf9.com")
	resp.set_cookie("samesite_strict", "dude3", samesite="Strict", domain="trieulieuf9.com")


	return resp


@app.route('/show-cookie')
def show_cookie():
	if request.headers.get("Host").lower() != "trieulieuf9.com":
		return f"{request.headers.get('Host').lower()} is not equal to trieulieuf9.com"

	return f"{request.headers.get('Cookie')}", 200



@app.route('/send_cookie_cross_site')
def send_cookie_cross_site():
	if request.headers.get("Host").lower() != "trieulieuf10.com":
		return f"{request.headers.get('Host').lower()} is not equal to trieulieuf10.com"

	html = """
		<a href="http://trieulieuf9.com/show-cookie">click me</a>
		hello dude
		<iframe src="http://trieulieuf9.com/show-cookie">
		<br>
		
	"""

	return html


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=80, debug=True)