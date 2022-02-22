import random

small_characters = 'abcdefghijlkmnoprqstuwyxz'
characters = {
    'small': small_characters,
    'big': small_characters.upper(),
    'numbers': '0123456789',
    'brackets': '{}[]<>()',
    'commas': ',.:;',
    'other': '!@#$%^&*-+*~`/'
}


def generate_password(settings):
    results = {}
    letters = select_letters(settings)
    if len(letters) > 0 and ('passwordLength' in settings.keys() and settings['passwordLength'] > 0):
        if has_true_key(settings, 'unique'):
            if 'passwordLength' in settings.keys() and settings['passwordLength'] <= len(letters):
                results['password'] = ''.join(random.sample(letters, settings['passwordLength']))
            else:
                results['error'] = 'Dla wybranych parametrów nie da się wygenrować hasła o zadanej długości'
        else:
            results['password'] = password_with_repeats(letters, settings['passwordLength'])
    else:
        results['error'] = 'Błąd nie wybrałeś znaków, z których wygenerować hasło albo długość hasła jest nieodpowiednia'
    return results


def select_letters(settings):
    letters = ''
    for key in characters.keys():
        if has_true_key(settings, key):
            letters += characters[key]
    return letters


def password_with_repeats(letters, length):
    password = []
    for i in range(length):
        password.append(letters[random.randrange(0, len(letters), 1)])
    return ''.join(password)


def has_true_key(settings, key):
    return key in settings.keys() and settings[key] == True
