#!/usr/bin/env python3.6

import sys
import argparse
from flask import Flask, request, render_template
import moogle
import util


app = Flask(__name__)
app.debug = True
app.db = None


@app.route("/")
def index():
    """Returns the index page."""
    return render_template("index.html", authors=moogle.authors())


@app.route("/search")
def search():
    """Returns the results page."""
    query = util.clean_words(request.args.get("query", ""))
    if query == "":
        return render_template("index.html")
    else:
        results = moogle.answer(app.db, query)
        return render_template("search.html", authors=moogle.authors(), query=query, results=results)


def main():
    parser = argparse.ArgumentParser(
        description="Web server module for the µoogle project",
        epilog=moogle.authors(),
    )

    parser.add_argument("-p", "--port", type=int, help="port where to listen", default=5000)
    parser.add_argument("-d", "--database", type=str, help="filename of the database", default="moogle.dat")

    args = parser.parse_args(sys.argv[1:])

    try:
        app.db = moogle.load(args.database)
    except Exception as e:
        print(e)

    app.run()


if __name__ == "__main__":
    main()
