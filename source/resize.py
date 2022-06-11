import configparser
import inputdata

config = configparser.ConfigParser()
config.read('config.ini')

win_width = 0
win_col = 0
def rescale_objects(event):
    global win_width, win_col
    maxcolumn = int(config.get('USERSETTING','maxcolumn'))
    try:
        event.widget.widgetName
    except Exception as e:
        if (win_width != event.width):
            win_width = event.width
            column = int((win_width - 106) / 214)
            if win_col != column:
                win_col = column
                if column >= 2 and column <= maxcolumn:
                    frameSpace = event.widget.nametowidget("!canvas.!frame.!frame")
                    frames = frameSpace.winfo_children()
                    for i in frames:
                        i.destroy()
                    inputdata.inData(frameSpace, column)
                if column == 1:
                    frameSpace = event.widget.nametowidget("!canvas.!frame.!frame")
                    frames = frameSpace.winfo_children()
                    for i in frames:
                        i.destroy()
                    inputdata.inData(frameSpace)