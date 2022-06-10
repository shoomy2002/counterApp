import os, csv, configparser
import frame

config = configparser.ConfigParser()
config.read('config.ini')

def inData(rootframe, col = None):
    path = config.get('USERSETTING', 'datafilepath')
    if os.path.exists(path):
        with open(path) as f:
            reader = csv.reader(f)
            if col is None:
                for row in reader:
                    frame.add_frame(rootframe, row[1], row[0])
            else:
                r, c = 0, 0
                for row in reader:
                    frame.add_frame(rootframe, row[1], row[0], r, c)
                    c += 1
                    if c == col:
                        r += 1
                        c = 0