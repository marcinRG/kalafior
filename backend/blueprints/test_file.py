import os

from flask import Blueprint, render_template, current_app

test_app = Blueprint('test_app', __name__)


@test_app.route("/test_app_test")
def test():
    imgs = current_app.config.get('APP_IMAGES')
    print(imgs)
    c_dir = os.getcwd()
    return c_dir
