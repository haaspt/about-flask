from flask import Flask, render_template
from AboutApp import app

AUTHOR = "Patrick Tyler Haas"
SITEURL = "literallyjustgraphs.com"
SITENAME = "Patrick Tyler Haas"

@app.route("/")
def about_me():
    const_dict = {
        "AUTHOR": AUTHOR,
        "SITEURL": SITEURL,
        "description": "My personal portfolio and developer's blog"
    }
    return render_template("index.html", **const_dict)

