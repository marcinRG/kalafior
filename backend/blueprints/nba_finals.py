from flask import Blueprint, render_template, request
import wikipedia
nba_finals_mvps = Blueprint('nba_finals_mvps', __name__)


@nba_finals_mvps.route('/finals_mvps')
def finals_mvps():
    wikipedia.set_lang('pl')
    page = wikipedia.page(pageid=333552, redirect=False)
    print(page.html())
    return page.html()
