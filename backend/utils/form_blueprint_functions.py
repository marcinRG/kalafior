import decimal

BMI_messages = {
    'severe_thinness': {'name': 'skrajne niedożywienie', 'description': 'Jesteś wygłodzony.'},
    'moderate_thinness': {'name': 'wychudzenie', 'description': 'Twój poziom BMI wskazuje na niedożywienie.'},
    'underweight': {'name': 'niedowaga', 'description': 'Według wskaźnika BMI masz niedowagę!'},
    'normal': {'name': 'normalna waga', 'description': 'Twoja waga znajduje się na normalnym posziomie.'},
    'overweight': {'name': 'nadwaga', 'description': 'Masz nadwagę.'},
    'obese_1': {'name': 'otyłość I stopnia', 'description': 'Masz poważną otyłość.'},
    'obese_2': {'name': 'otyłość II stopnia (duża)',
                'description': 'Masz bardzo dużą otyłość. Najlepiej skontaktuj się z lekarzem.'},
    'obese_3': {'name': 'otyłość III stopnia (chorobliwa)',
                'description': 'Twoja otyłość jest niebezpieczna dla zdrowia.'},
}

length_measurements = {
    'm': {'name': 'metr', 'scale': decimal.Decimal(1)},
    'mm': {'name': 'milimetr', 'scale': decimal.Decimal(0.001)},
    'cm': {'name': 'centymetr', 'scale': decimal.Decimal(0.01)},
    'km': {'name': 'kilometr', 'scale': decimal.Decimal(1000)},
    'mil': {'name': 'mila', 'scale': decimal.Decimal(1609)},
    'in': {'name': 'cal', 'scale': decimal.Decimal(0.0254)},
}

weight_measurements = {
    'g': {'name': 'gram', 'scale': decimal.Decimal(1)},
    'dg': {'name': 'dekagram', 'scale': decimal.Decimal(10)},
    'kg': {'name': 'kilogram', 'scale': decimal.Decimal(1000)},
    't': {'name': 'tona', 'scale': decimal.Decimal(1000000)},
    'oz': {'name': 'uncja', 'scale': decimal.Decimal(28.349)},
    'lb': {'name': 'funt', 'scale': decimal.Decimal(453.592)},
    'st': {'name': 'kamień', 'scale': decimal.Decimal(6350)},
}


def get_BMI_message(BMI):
    if BMI < 16:
        return BMI_messages['severe_thinness']
    elif BMI < 17:
        return BMI_messages['moderate_thinness']
    elif BMI < 18.5:
        return BMI_messages['underweight']
    elif BMI < 25:
        return BMI_messages['normal']
    elif BMI < 30:
        return BMI_messages['overweight']
    elif BMI < 35:
        return BMI_messages['obese_1']
    elif BMI < 40:
        return BMI_messages['obese_2']
    else:
        return BMI_messages['obese_3']


def calculate_BMI(weight, height):
    return weight / ((height / 100) ** 2)


def measurements_conversion(unit_type, amount, input, output):
    if unit_type == 'mass':
        return calculate_conversion(weight_measurements, amount, input, output)
    elif unit_type == 'length':
        return calculate_conversion(length_measurements, amount, input, output)


def calculate_conversion(converesion_table, amount, input, output):
    return decimal.Decimal(amount) * (converesion_table[input])['scale'] / (converesion_table[output])['scale']


def get_unit_name(unit_type, unit):
    if unit_type == 'mass':
        return weight_measurements[unit]['name']
    elif unit_type == 'length':
        return length_measurements[unit]['name']
