from flask import Flask, send_from_directory, request, render_template, render_template_string, jsonify, make_response
app = Flask(__name__)


@app.route('/xss')
def xss():
	html = """
		<h3 id="hello">hello dude</h3>
		<iframe src="http://localhost:8000/static/xss_sandbox.svg" style="width: 100%; height: 100%">
	"""
	return html, 200


@app.route('/xss_sandbox')
def xss_sandbox():
	html = """
		<h3 id="hello">hello dude</h3>
		<iframe sandbox src="http://localhost:8000/static/xss_sandbox.svg" style="width: 100%; height: 100%">
		<!-- <iframe sandbox="allow-same-origin allow-scripts allow-modals" src="http://localhost:8000/static/xss_sandbox.svg" style="width: 100%; height: 100%"> --!>
	"""
	return html, 200


@app.route('/laugh')
def billion_laugh():
	html = """
		<button onclick=alert("hello")>hello</button
		<!-- <img src="static/biilion_laugh_svg_xlink.svg"> --!>
		<!-- <img src="static/normal_image.jpg"> --!>
		<iframe sandbox src="static/biilion_laugh_svg_xlink.svg" style="width: 100%; height: 100%">
		<!-- <iframe src="static/normal_image.jpg" style="width: 100%; height: 100%"> --!>
	"""
	return html, 200


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000, debug=True)