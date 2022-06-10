import csv, configparser
import frame

config = configparser.ConfigParser()
config.read('config.ini')

def outData(rootFrame):
    frames = rootFrame.nametowidget("!canvas.!frame.!frame").winfo_children()
    path = config.get('USERSETTING', 'datafilepath')
    with open(path, mode='w', newline='') as f:
        writer = csv.writer(f)
        if len(frames) > 0:
            for i in range(frame.getFrameNum()):
                children = frames[i].winfo_children()
                for c in children:
                    if c.winfo_name() == '!entry':
                        name = c.get()
                    if c.winfo_name() == '!label':
                        count = c['text']
                writer.writerow([name, count])