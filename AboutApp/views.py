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

    interests = [
        "Proin sed sem sed est tempor facilisis non sed ex.",
        "Maecenas pretium nibh sagittis urna tincidunt congue.",
        "Curabitur tristique leo id libero dapibus, dapibus lacinia magna porttitor.",
        "Morbi pellentesque turpis eget arcu fringilla condimentum ut ut metus."
    ]

    skills = [
        "Aenean non lorem lobortis, porttitor augue vitae, dapibus lectus.",
        "Suspendisse sit amet orci eu est imperdiet rutrum nec a erat.",
        "Phasellus consectetur enim tincidunt accumsan rhoncus.",
        "Duis sed quam vestibulum tortor semper suscipit non ut sapien.",
        "Vivamus at neque volutpat, semper libero ac, tincidunt velit."
    ]

    return render_template("about.html",
                           projects=projects,
                           skills=skills,
                           interests=interests,
                           **attr_dict)

@app.route("/contact")
def contact():

    attr_dict = {
        "AUTHOR": AUTHOR,
        "SITEURL": SITEURL,
        "title": "PTH — Contact",
        "description": "My personal portfolio and developer's blog"
    }

    return render_template("contact.html", **attr_dict)

