from tkinter import *
from tkinter import ttk
import ttkbootstrap
import pytube
import threading
import time
import sys


root = Tk()
root.title('PyTube Downloader')
root.resizable(width=False, height=False)
ttkbootstrap.Style(theme="cosmo")
url_entry = Entry(root, width=50, borderwidth=5)
file_path_entry = Entry(root, width=50, borderwidth=5)
file_path_entry.insert(0, 'Save path:')
itag_entry = Entry(root, width=50, borderwidth=5)


def set_file_path():
    global SAVE_PATH
    SAVE_PATH = file_path_entry.get()
    file_path_entry.destroy()
    set_file_path_button.destroy()
    
    url_entry.grid(row=0, column=0, columnspan=3)
    url_entry.insert(0, 'Link:')
    set_url_button.grid(row=1, column=1)


def set_url():
    global url
    global yt
    url = url_entry.get()
    url_entry.destroy()
    set_url_button.destroy()
    
    yt = pytube.YouTube(url)
    stream_var = str(yt.streams)
    spl = stream_var.split(",")
    textbox_variable = ("\n\n".join([",".join(spl[i:i+1]) for i in range(0,len(spl),1)]))
    
    text=Text(root, width=80, height=15, borderwidth=5)
    text.insert(END, textbox_variable)
    text.grid(row=2, column=1)
    
    itag_entry.grid(row=0, column=0, columnspan=3)
    itag_entry.insert(0, 'Itag:')
    set_itag_button.grid(row=1, column=1)


def set_itag():
    global itag_id
    itag_id = itag_entry.get()
    
    itag_entry.destroy()
    set_itag_button.destroy()

    threading.Thread(target=download, daemon=True).start()
    label_1.grid(row=0, column=0, columnspan=3)
    
    quitting_in = 5
    for _ in range(5):
        time.sleep(1)
        quitting_in -= 1
        label_1.config(text=f'Done\nQutting: {quitting_in} seconds')
    root.destroy()
    sys.exit()


def download():
    d_video = yt.streams.get_by_itag(itag_id)
    d_video.download(SAVE_PATH)


def start_file_thread():
    threading.Thread(target=set_file_path, daemon=True).start()
def start_url_thread():
    threading.Thread(target=set_url, daemon=True).start()
def start_itag_thread():
    threading.Thread(target=set_itag, daemon=True).start()


set_file_path_button = ttk.Button(root, text='Set Save Path', style='Outline.TButton', command=start_file_thread)
set_url_button = ttk.Button(root, text='Set link', style='Outline.TButton', command=start_url_thread)
set_itag_button = ttk.Button(root, text='Set itag and download', style='Outline.TButton', command=start_itag_thread)
label_1 = Label(root, text=' \n')

file_path_entry.grid(row=0, column=0, columnspan=3)
set_file_path_button.grid(row=1, column=1)


root.mainloop()
