from flask import Blueprint, render_template, jsonify
from utils.import_text_to_list import import_text_to_list

kubus = Blueprint('kubus', __name__)


@kubus.route("/kubus_puchatek")
def puchatek():
    return render_template('puchatek/puchalke.html')


@kubus.route("/kubus_puchatek/data")
def puchatek_data():
    txt_data = import_text_to_list('resources/kubus_puchatek/kubus_puchatek.txt')
    response = jsonify(
        author="A. A. MILNE",
        title="'Kubuś Puchatek",
        text=txt_data
    )
    return response
