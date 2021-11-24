import youtube_dl
import threading
from ttkbootstrap import *
from tkinter import *


root = Tk()
root.title('Youtube-DL GUI')
style = Style(theme='cosmo')
root.resizable(width=False, height=False)


url_entry = Entry(root, width=35, borderwidth=5)
url_entry.insert(0, 'Link: ')
working_label = Label(root, text='')


def main():
    url = url_entry.get()
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def start_thread():
    threading.Thread(target=main).start()


run_button = Button(root, text='Run', width=20, borderwidth=5, command=start_thread)


url_entry.grid(row=0, column=0, columnspan=3)
working_label.grid(row=1, column=1)
run_button.grid(row=1, column=1)


root.mainloop()
