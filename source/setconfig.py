import configparser
import pyautogui as pag

config = configparser.ConfigParser()

def create():
    monitorx, monitory = pag.size()
    x = 340
    y = 200
    posx = int(monitorx/2-x/2)
    posy = int(monitory/2-y/2)
    winpos = f'{x}x{y}+{posx}+{posy}'
    config['DEFAULT'] = {
        'datafilepath': './data.csv',
        'initCount': '0',
        'winpos': winpos,
        'maxcolumn': 3
        }

    config['USERSETTING'] = {}

    with open('config.ini', 'w') as f:
        config.write(f)