import os

from flask import Flask, request, render_template
from models import create_post, get_posts


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "GET":
        pass

    if request.method == "POST":
        name = request.form.get("name")
        post = request.form.get("post")
        create_post(name, post)

    posts = get_posts()
    return render_template("index.html", posts=posts)

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get("host", "0.0.0.0")
    port = int(os.environ.get("port", 1234))
    app.run(host=host, port=port)