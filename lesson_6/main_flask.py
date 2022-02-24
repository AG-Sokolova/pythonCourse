from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index():
    return "The first flask Page!"