from flask import Flask, render_template, request
import create_map as cm

app = Flask(__name__)


@app.route("/")
def hello(name=None):
    """

    :return:
    """
    return render_template("index.html", name=name)


@app.route("/application", methods=["POST"])
def application():
    """
    :return:
    """
    if request.form['name'] and request.form['counter']:
        int(request.form['counter'])
        cm.create_map(request.form['name'], request.form['counter'])
        return render_template("Map.html")


if __name__ == "__main__":
    app.run(debug=True)
