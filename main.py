import requests, json

URL = "http://127.0.0.1:8000/product/"

# r = requests.get(URL)
# data = r.text
# jasonas = json.loads(data)
# print(type(data))
# print(data)
# print(type(jasonas))
# print(jasonas)
# for i in jasonas:
#     print(i['code'])
def irasu_grazintojas(id):
    uzklausa = requests.get(f'{URL}{id}')
    duomenys = json.loads(uzklausa.text)
    return duomenys
#
def duomenu_rasytojas(duomenys):
    data = json.dumps(duomenys)
    padavimas = requests.post(f'{URL}', data=data)
    print(padavimas.status_code)

#
#
ikelt = {'name': 'Shirt1', 'color': 'Blue1', 'description': 'Beutiful1', 'price': '600.00'}
# duomenys = {'name': 'Boruzes skraido'}
# print(irasu_grazintojas(1))
duomenu_rasytojas(ikelt)