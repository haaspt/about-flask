from flask import Flask, render_template
from AboutApp import app

AUTHOR = "Patrick Tyler Haas"
SITEURL = "literallyjustgraphs.com"
SITENAME = "Patrick Tyler Haas"

@app.route("/")
def about_me():
    attr_dict = {
        "AUTHOR": AUTHOR,
        "SITEURL": SITEURL,
        "title": "PTH — Portfolio",
        "description": "My personal portfolio and developer's blog"
    }

    projects = [
        {"project_title": "Lorem Ipsum",
         "project_desc": "Donec finibus rutrum massa vitae rutrum. Nulla facilisi.",
         "project_link": "#"},
         {"project_title": "Lorem Ipsum",
         "project_desc": "Suspendisse sit amet orci eu est imperdiet rutrum nec a erat.",
         "project_link": "#"},
         {"project_title": "Lorem Ipsum",
         "project_desc": "Duis sed quam vestibulum tortor semper suscipit non ut sapien. Integer ac lacus sit amet diam dictum ornare.",
         "project_link": "#"}
    ]

    return render_template("about.html", projects=projects, **attr_dict)

@app.route("/contact")
def contact():

    attr_dict = {
        "AUTHOR": AUTHOR,
        "SITEURL": SITEURL,
        "title": "PTH — Contact",
        "description": "My personal portfolio and developer's blog"
    }

    return render_template("contact.html", **attr_dict)

