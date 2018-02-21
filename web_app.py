from flask import Flask, render_template, request
import create_map as cm
from urllib.error import HTTPError

app = Flask(__name__)


@app.route("/")
def hello(name=None):
    """
    (None -> html)
    This function calls page index.html
    returns: index.html page
    """

    return render_template("index.html", name=name)


@app.route("/application", methods=["POST"])
def application():
    """
    () -> (html)
    This function uses html queries type of "GET" and
    builds a web map
    returns: html map with markers of user`s friends
    """

    try:
        if not request.form['name'] or not request.form['counter']:
            raise ValueError
        elif request.form['name'] and request.form['counter']:
            int(request.form['counter'])
            cm.create_map(request.form['name'], request.form['counter'])
            return render_template("Map.html")
    except (ValueError, HTTPError):
        return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)
