from flask import Flask, send_from_directory, request, render_template, render_template_string, jsonify, make_response
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!!!\n', 200


@app.route('/upload', methods=['GET'])
def upload_file_get():
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h3>Normal Upload</h3>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <br>
    <br>
    <h3>Upload with fetch</h3>
    <button id=upload-btn>upload with fetch()</button>
    <script>
        document.getElementById("upload-btn").onclick = function() {
          fetch('/upload', {
          method: 'POST',
          headers: {
            "Content-Type": "multipart/form-data; boundary=---------------------------3297732952069655358128090298"
          },
          body: `-----------------------------3297732952069655358128090298
Content-Disposition: form-data; name="file"; filename="hello5.txt"
Content-Type: text/plain

hello_dude

-----------------------------3297732952069655358128090298--`,
        }).then(response => response.text())
        .then(text => console.log(text))
        }
    </script>
    """

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file:
        filename = file.filename
        # filename = secure_filename(file.filename)
        file.save(f"upload/{filename}")
        return f"uploaded: ${filename}"

    return "hee"


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000, debug=True)