import tkinter as tk
import tkinter.simpledialog as simpledialog
import os, tkinter.filedialog, configparser
import outputdata

config = configparser.ConfigParser()
config.read('config.ini')

def open_file(event = None):
    fTyp = [('テキストファイル', "*.csv"), ('すべてのファイル', "*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    selectedFilePath = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir = iDir)
    config.set('USERSETTING', 'datafilepath', selectedFilePath)
    with open('config.ini', 'w') as f:
        config.write(f)

def save(rootFrame, event = None): outputdata.outData(rootFrame)

def exit(rootFrame):
    winx, other = rootFrame.geometry().split("x")
    winy, posx, posy = other.split("+")
    config.set('USERSETTING', 'winx', winx)
    config.set('USERSETTING', 'winy', winy)
    config.set('USERSETTING', 'posx', posx)
    config.set('USERSETTING', 'posy', posy)
    with open('config.ini', 'w') as f:
        config.write(f)
    rootFrame.destroy()

def setinitcount():
    initcount = config.get('USERSETTING','initcount')
    getinitcount = simpledialog.askinteger("初期値設定", "設定するカウンターの初期値を入力してください\n(再起動で反映)", initialvalue=initcount, minvalue=0)
    if getinitcount is not None:
        config.set('USERSETTING', 'initcount', str(getinitcount))
        with open('config.ini', 'w') as f:
            config.write(f)

def setmaxcolumn():
    maxcolumn = config.get('USERSETTING','maxcolumn')
    getmaxcolumn = simpledialog.askinteger("表示列設定", "最大の表示列数を入力してください\n(再起動で反映)", initialvalue=maxcolumn, minvalue=1)
    if getmaxcolumn is not None:
        config.set('USERSETTING', 'maxcolumn', str(getmaxcolumn))
        with open('config.ini', 'w') as f:
            config.write(f)

def make_menu(rootFrame):
    # 親メニュー
    menubar = tk.Menu(rootFrame)
    rootFrame.config(menu=menubar)
    # ファイルメニュー
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='ファイル', menu=file_menu)
    file_menu.add_command(label='開く', command=open_file, accelerator="Ctrl+O")
    rootFrame.bind("<Control-Key-o>", open_file)
    file_menu.add_command(label='保存', command=lambda:save(rootFrame), accelerator="Ctrl+S")
    rootFrame.bind("<Control-Key-s>", save(rootFrame))
    file_menu.add_command(label='名前をつけて保存')
    file_menu.add_command(label='終了', command=lambda:exit(rootFrame))

    # # 編集メニュー
    # edit_menu = tk.Menu(menubar, tearoff=0)
    # menubar.add_cascade(label='編集', menu=edit_menu)

    # 設定メニュー
    setting_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='設定', menu=setting_menu)
    setting_menu.add_command(label='初期値設定', command=setinitcount)
    setting_menu.add_command(label='表示列設定', command=setmaxcolumn)