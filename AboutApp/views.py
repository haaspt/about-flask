from flask import Flask, render_template
from AboutApp import app

AUTHOR = "Patrick Tyler Haas"
SITEURL = "literallyjustgraphs.com"
SITENAME = "Patrick Tyler Haas"
SITESUBTITLE = "A little about me"

@app.route("/")
def main():
    return render_template("index.html", title="Test!")

