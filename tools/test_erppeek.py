import erppeek
import csv

username = 'lpdip'  # The Odoo user
pwd = 'azerty&1785'  # The password of the Odoo user
dbname = "firstOne"  # The Odoo database
server = 'http://127.0.0.1:8071'

client_erppeek = erppeek.Client(server, dbname, username, pwd)
proxy = client_erppeek.model('iut.agenda')


def get_all_data_serial():
    serial_element = list()
    model_serial_data = client_erppeek.model('iut.device')
    model_serial_browse = model_serial_data.browse([])
    for field_data in model_serial_browse:
        serial_element.append(field_data.serial_number)
    return serial_element


def get_all_data_model():
    model_name_element = list()
    model_type_element = list()
    model_serial_data = client_erppeek.model('iut.model')
    model_serial_browse = model_serial_data.browse([])
    for field_data in model_serial_browse:
        model_name_element.append(field_data.name)
        print('IDS', field_data.type_ids)
    type_device_search = client_erppeek.model('iut.model.type')
    model_serial_browse = type_device_search.browse([])
    for field_data in model_serial_browse:
        model_type_element.append(field_data.name)
        print('ID', field_data.id)
    return model_name_element, model_type_element


def insert_data_model_into_model(model_data, id_type, list_model_name):
    if model_data in list_model_name:
        print('champ name_model déjà existant')
        msg_return = 1

    else:
        model_serial_data = client_erppeek.model('iut.model')

        model_serial_data.create({'name': model_data,
                                  'ref': model_data,
                                  'type_ids': id_type})
        print('model ajouté')
        msg_return = 0
    return msg_return


def insert_data_serial_into_model(serial_data,  model_data, type_device_data, date_alloc_data, date_buy_data,
                                  list_to_compare):

    model_serial_data = client_erppeek.model('iut.device')
    if serial_data in list_to_compare:
        print('champ serial déjà existant')
    else:
        print('champ ajouté')
        model_serial_data.create({'name': model_data + '_' + type_device_data + '_' + serial_data,
                                 'serial_number': serial_data,
                                  'date_allocation': date_alloc_data,
                                  'date_purchase': date_buy_data})


with open('/home/dorian/Documents/datacsv.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    serial = ''
    date_alloc = ''
    date_buy = ''
    model = ''
    marque = ''
    type_device = ''
    employe = ''
    id_model_type = ''
    list_serial = get_all_data_serial()
    list_model, list_type = get_all_data_model()
    for row in reader:
        serial = row['Numéro de série']
        date_alloc = row['Date allocation']
        date_buy = row['Date achat']
        model = row['Modèle']
        marque = row['Marque']
        type_device = row['Type']
        employe = row['Employé']
        model_serial = client_erppeek.model('iut.model.type')
        if type_device not in list_type:
            model_serial.create({'name': type_device})
            id_model_type = model_serial.search([('name', '=', type_device)])
            print('type ajouté')
        else:
            id_model_type = model_serial.search([('name', '=', type_device)])
        msg = insert_data_model_into_model(model, id_model_type, list_model)
        if int(msg) != 1:
            insert_data_serial_into_model(serial, model, type_device, date_alloc, date_buy, list_serial)
        else:
            print('errors')
