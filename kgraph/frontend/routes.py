from flask import Blueprint, render_template

from . import route

bp = Blueprint('main', __name__)

@route(bp, '/')
def main():
    return render_template('main.html')