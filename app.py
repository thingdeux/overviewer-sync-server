from flask import Flask, request, flash, url_for, redirect, \
    render_template, abort, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

if __name__ == "__main__":
    app.run()