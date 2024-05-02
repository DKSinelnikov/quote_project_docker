from flask import Flask, randem_templates, jsonify
from utils import get_quotes_authors, get_random_quote
filename = "quotes.txt"

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello. Добро пожалуй. "


@app.route("/random")
def random_quote():
    return jsonify(get_random_quote(filename))

if __name__ == "__name__":
    app.run()