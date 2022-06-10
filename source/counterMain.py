import tkinter as tk
from tkinter import ttk
import os, setconfig, configparser, scroll

if not os.path.exists('config.ini'): setconfig.create()

import menu, frame, inputdata, resize

config = configparser.ConfigParser()
config.read('config.ini')

root = tk.Tk()
winx = int(config.get('USERSETTING', 'winx'))
winy = int(config.get('USERSETTING', 'winy'))
posx = int(config.get('USERSETTING', 'posx'))
posy = int(config.get('USERSETTING', 'posy'))
root.geometry(f'{winx}x{winy}+{posx}+{posy}')
root.minsize(320, 200)
root.title('カウンター')

# 追加予定機能
# 行消去ボタン無効化
# 編集＞カウント一括変更


initCount = config.get('USERSETTING', 'initcount')
sizegrip = ttk.Sizegrip(root)
sizegrip.pack(side='bottom', anchor='se')
ttk.Button(root, text = "+", width=5, command = lambda:frame.add_frame(frameSpace, initCount)).pack(side='left', anchor='n', padx=20, pady=20)
frameSpace = tk.Frame(scroll.ScrollableFrame(root).scrollable_frame)
frameSpace.pack(anchor='w', pady=15)
inputdata.inData(frameSpace)

root.bind("<Configure>", resize.rescale_objects)
menu.make_menu(root)

def callback():
    menu.exit(root)

root.protocol("WM_DELETE_WINDOW", callback)
root.mainloop()
