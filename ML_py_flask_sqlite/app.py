import os

from flask import Flask, render_template, request
from models import create_LR, get_salary

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "GET":
        pass

    if request.method == "POST":
        years_of_exp = request.form.get("experiences")
        create_LR(years_of_exp)

    experiences = get_salary()
    return render_template('index.html', salary=experiences)

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get("host", "0.0.0.0")
    port = int(os.environ.get("port", 1234))
    app.run(host=host, port=port)