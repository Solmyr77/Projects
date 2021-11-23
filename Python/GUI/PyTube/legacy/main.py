from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import ttkbootstrap
import pytube
import threading
import time
import sys
import os


root = Tk()
root.title('PyTube Downloader')
root.resizable(width=False, height=False)
ttkbootstrap.Style(theme="cosmo")
url_entry = Entry(root, width=50, borderwidth=5)
itag_entry = Entry(root, width=50, borderwidth=5)
curr_directory = os.getcwd()


def set_file_path():
    global SAVE_PATH
    SAVE_PATH = fd.askdirectory()
    set_file_path_button.destroy()
    
    url_entry.grid(row=0, column=0, columnspan=3)
    set_url_button.grid(row=1, column=1)


def set_url():
    global url
    global yt
    url = url_entry.get()
    url_entry.destroy()
    set_url_button.destroy()
    
    yt = pytube.YouTube(url)
    stream_var_video = str(yt.streams.order_by('resolution').desc())
    stream_var_audio = str(yt.streams.filter(only_audio=True))
    spl_1 = stream_var_video.split(",")
    spl_2 = stream_var_audio.split(",")
    textbox_video_variable = ("\n\n".join([",".join(spl_1[i:i+1]) for i in range(0,len(spl_1),1)]))
    textbox_audio_variable = ("\n\n".join([",".join(spl_2[i:i+1]) for i in range(0,len(spl_2),1)]))
    thumb = (f'\nThumbnail url: {yt.thumbnail_url}\n\n')
    
    text=Text(root, width=80, height=15, borderwidth=5)
    text.insert(END, thumb)
    text.insert(END, textbox_video_variable)
    text.insert(END, '\n\n')
    text.insert(END, textbox_audio_variable)
    text.grid(row=3, column=1)
    
    label_2.grid(row=2, column=1)
    itag_entry.grid(row=0, column=0, columnspan=3)
    set_itag_button.grid(row=1, column=1)


def set_itag():
    global itag_id, itag_id2
    itag_id, itag_id2 = map(int, itag_entry.get().split(','))
    
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
    global name_video
    global name_audio
    d_video_1 = yt.streams.get_by_itag(itag_id)
    d_video_2 = yt.streams.get_by_itag(itag_id2)
    video_name_1 = d_video_1.default_filename
    video_name_2 = d_video_2.default_filename
    extension_1 = os.path.splitext(video_name_1)
    extension_2 = os.path.splitext(video_name_2)
    
    name_video = f'Video_{yt.title}{extension_1[1]}'
    name_audio = f'Audio_{yt.title}{extension_2[1]}'
    
    d_video_1.download(SAVE_PATH, filename=name_video)
    d_video_2.download(SAVE_PATH, filename=name_audio)
    

def start_file_thread():
    threading.Thread(target=set_file_path, daemon=True).start()
def start_url_thread():
    threading.Thread(target=set_url, daemon=True).start()
def start_itag_thread():
    threading.Thread(target=set_itag, daemon=True).start()


set_file_path_button = ttk.Button(root, text='Set Save Path', style='Outline.TButton', command=start_file_thread)
set_url_button = ttk.Button(root, text='Set link', style='Outline.TButton', command=start_url_thread)
set_itag_button = ttk.Button(root, text='Set itags and download', style='Outline.TButton', command=start_itag_thread)
label_2 = Label(root, text="Requires two Itags separated with a comma (video, audio)")
label_1 = Label(root, text=' \n')


set_file_path_button.grid(row=1, column=1)


root.mainloop()
