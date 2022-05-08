from flask import Blueprint, render_template, request
from werkzeug.utils import redirect
import html

from TripsDb.TripsFormDb import TripFormsDb
from utils.form_blueprint_classes import BMIForm, MeasurementForm, TripForm
from utils.form_blueprint_functions import calculate_BMI, get_BMI_message, measurements_conversion, get_unit_name


test_forms = Blueprint('test_forms', __name__)

db = TripFormsDb('sqlite:///resources/forms/test.db')

known_routes = ['description', 'BMI', 'measures', 'trip']


def get_page(page):
    if page and page is not None:
        results = [element for element in known_routes if element == page]
        if len(results) > 0:
            return results[0]
    return 'description'


@test_forms.route('/forms')
def forms():
    return redirect('forms/description')


@test_forms.route('/forms/<page>', methods=['POST', 'GET'])
def forms_test(page):
    form = None
    results = None
    if page == 'BMI':
        form = BMIForm()
        if request.method == 'POST' and form.validate():
            bmi = calculate_BMI(form.weight.data, form.height.data)
            msg = get_BMI_message(bmi)
            results = {'bmi': bmi,
                       'name': msg['name'], 'txt': msg['description']}
    if page == 'measures':
        form = MeasurementForm()
        if request.method == 'POST' and form.validate():
            unit = form.measurement_select.data
            if unit == 'length':
                input = form.measures_length_input.data
                output = form.measures_length_output.data
            if unit == 'mass':
                input = form.measures_mass_input.data
                output = form.measures_mass_output.data
            quantity = form.measurement_quantity.data
            amount = measurements_conversion(unit, quantity, input, output)
            results = {'input': quantity, 'output': amount, 'input_unit': get_unit_name(
                unit, input), 'output_unit': get_unit_name(unit, output)}

    if page == 'trip':
        results = db.show_all_trips()
        form = TripForm()
        if request.method == 'POST' and form.validate():
            db.add_new_trip({
                'direction': html.escape(form.trip_direction.data),
                'description': html.escape(form.trip_description.data),
                'name': html.escape(form.name.data)
            })
            return redirect('/forms/{}'.format(page))

    page_form = get_page(page)
    return render_template('/forms/' + page_form + '.html', page_form=page_form, form=form, results=results)
