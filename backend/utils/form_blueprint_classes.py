from email.policy import default
from flask_wtf import FlaskForm
from wtforms import IntegerField, validators, RadioField, SelectField, DecimalField, StringField, TextAreaField, ValidationError

length_collection = [('m', 'metr'), ('mm', 'milimetr'), ('cm', 'centymetr'), ('km', 'kilometr'), ('in', 'cal'),
                     ('mil', 'mila')]
mass_collection = [('g', 'gram'), ('dg', 'dekagram'), ('kg', 'kilogram'), ('t', 'tona'), ('oz', 'uncja'),
                   ('lb', 'funt'), ('st', 'kamień')]

trip_directions = [('mountains', 'w góry'),
                   ('wyjazd nad morze', 'nad morze'),
                   ('wyjazd do miasta',
                    'miasto lub inna miejscowość'),
                   ('inne', 'inne'),
                   ('zostaję w domu', 'zostaję w domu')]


class BMIForm(FlaskForm):
    height = IntegerField('Podaj wzrost (cm):', [validators.InputRequired(message='Musisz wypełnić to pole'),
                                                 validators.NumberRange(
                                                     message='Podaj wartość z przedziału od 90 do 320', min=90,
                                                     max=320)])
    weight = IntegerField('Podaj wagę (kg):', [validators.InputRequired(message='Musisz wypełnić to pole'),
                                               validators.NumberRange(message='Podaj wartość z przedziału od 35 do 550',
                                                                      min=35, max=550)])


class MeasurementForm(FlaskForm):
    measurement_quantity = DecimalField('Podaj ilość do konwersji',
                                        [validators.InputRequired('Musisz wypełnić to pole'),
                                         validators.NumberRange(message='Podana wartość musi być większa od 0', min=0)])
    measurement_select = RadioField('Wybierz co chcesz przeliczać:', choices=[
                                    ('length', 'długość'), ('mass', 'masa')], default='length')

    measures_length_input = SelectField('Wybierz jednostkę wejściową:',
                                        choices=length_collection)

    measures_length_output = SelectField('Wybierz jednostkę wyjściową:',
                                         choices=length_collection)

    measures_mass_input = SelectField('Wybierz jednostkę wejściową:',
                                      choices=mass_collection)

    measures_mass_output = SelectField('Wybierz jednostkę wyjściową:',
                                       choices=mass_collection)


class TripForm(FlaskForm):
    trip_direction = SelectField(
        'Gdzie jedziesz na majówkową wycieczkę?', choices=trip_directions)
    trip_description = TextAreaField(
        'Krótki opis:', [validators.InputRequired(message='Musisz wypełnić to pole'), validators.Length(max=120, message='Pole może zawierać jedynie {} znaków!'.format(120))])
    name = StringField('Twoje imię:', [validators.InputRequired(
        message='Musisz wypełnić to pole'), validators.Length(max=35, message='Pole może zawierać jedynie {} znaków!'.format(35))])
