from flask import Flask, send_from_directory, request, render_template, render_template_string, jsonify, make_response
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!!!\n', 200


@app.route('/file/<path:file_path>')
def path_traversal(file_path):
	print("path:", file_path)
	try:
		with open(file_path) as file:
		# with open("../.gitignore") as file:
			return f"<pre>{file.read()}</pre>\n"
	except Exception as e:
		return f"<pre>Internal Server Error\n\nPath: {file_path}\n\n{e}</pre>\n", 500


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000, debug=True)