from flask import Flask, render_template
from AboutApp import app

@app.route("/")
def main():
    return render_template("index.html", title="Test!")

