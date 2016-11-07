import string
my_dict = {
    'privet': ' I Tebe privet, Detka',
    'kak dela?': 'Luche vseh',
    'poka': 'uvidimsya, malish'
}

def get_answer(key, my_dict):
    return str(my_dict.get(key).lower().strip())

print(get_answer('privet', my_dict))