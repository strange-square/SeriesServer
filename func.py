import requests
from json import dumps, loads

def get_url(main_args, method):
    return f'http://{main_args.host}:{main_args.port}/{method}'

def graceful_exit():
    ack = input('Are you sure you want to leave (Y/N)?')
    if ack == 'Y':
        print('Goodbye!')
        exit()
    elif ack == 'N':
        print('OK, let\'s continue')
    else:
        print('Incorrect input')

def help():
    print("Commands:")
    print("add series | add series to watched | add series to to-see list")
    print("get episode | set episode | get raiting | set raiting")
    print("generate serias | series watched | series to to-see list")
    print("exit")

'''''''''''''''''''''''''''''''''POST'''''''''''''''''''''''''''''''''
def add_series(main_args):
    name = input('Print name:')
    size = input('Print number of episods:')

    try:
        name, size = str(name), int(size)
        requests.post(get_url(main_args, 'add'), 
            params=dict(name = name, size = size))
    except ValueError:
        print('Incorrect input')


def add_to_watched(main_args):
    name = input('Print name:')

    try:
        name = str(name)
        resp = requests.post(get_url(main_args, 'add2watched'), 
            params=dict(name = name))
    except:
        print('Incorrect input')

    if resp.text == "not at list":
        print('You can only add series from the main list')
    if resp.text == "double":
        print('Already in the list')


def add_to_see(main_args):
    name = input('Print name:')

    try:
        name = str(name)
        resp = requests.post(get_url(main_args, 'add2see'), 
            params=dict(name = name))
    except:
        print('Incorrect input')

    if resp.text == "not at list":
        print('You can only add series from the main list')
    if resp.text == "double":
        print('Already in the list')


'''''''''''''''''''''''''''''''''POST-GET'''''''''''''''''''''''''''''''''
def get_episode(main_args):
    name = input('Print name:')

    try:
        name = str(name)
        print(requests.get(get_url(main_args, 'episode'), 
            data=dict(name = name)).text)
    except:
        print('Incorrect input')

def set_episode(main_args):
    name = input('Print name:')
    num = input('Print number of watched episodes:')

    try:
        name, num = str(name), int(num)
        print(requests.post(get_url(main_args, 'episode'), 
            params=dict(name = name, num = num)).text)
    except:
        print('Incorrect input')

def get_raiting(main_args):
    name = input('Print name:')

    try:
        name = str(name)
        print(requests.get(get_url(main_args, 'raiting'), 
            data=dict(name = name)).text)
    except:
        print('Incorrect input')

def set_raiting(main_args):
    name = input('Print name:')
    rait = input('Print your raiting:')

    try:
        name, rait = str(name), int(rait)
        print(requests.post(get_url(main_args, 'raiting'), 
            params=dict(name = name, rait = rait)).text)
    except:
        print('Incorrect input')


'''''''''''''''''''''''''''''''''GET'''''''''''''''''''''''''''''''''
def print_list(l):
    for name in l:
        print(name)

def gen_serias(main_args):
    print(requests.get(get_url(main_args, 'generator')).text)

def get_watched(main_args):
    l = loads(requests.get(get_url(main_args, 'watched')).text)
    print_list(l)

def get_to_see(main_args):
    l = loads(requests.get(get_url(main_args, '2see')).text)
    print_list(l)
