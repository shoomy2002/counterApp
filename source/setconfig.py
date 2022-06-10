import configparser
import pyautogui as pag

config = configparser.ConfigParser()

def create():
    x = 340
    y = 200
    monitorx, monitory = pag.size()
    posx = int(monitorx/2-x/2)
    posy = int(monitory/2-y/2)
    config['DEFAULT'] = {
        'datafilepath': './data.csv',
        'initCount': '0',
        'posx': posx,
        'posy': posy,
        'winx': x,
        'winy': y,
        'maxcolumn': 3
        }

    config['USERSETTING'] = {}

    with open('config.ini', 'w') as f:
        config.write(f)