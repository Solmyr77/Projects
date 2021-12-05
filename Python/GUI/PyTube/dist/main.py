from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import ttkbootstrap
import pytube
import threading
import os


root = Tk()
root.title('PyTube Downloader')
root.resizable(width=False, height=False)
ttkbootstrap.Style(theme="cosmo")


class Downloader:


    def __init__(self):
        self.SAVE_PATH = None
        self.url = None
        self.yt = None
        self.itag_id = None
        self.itag_id2 = None
        self.url_entry = None
        self.itag_entry = None
        self.single_itag_id = None
        self.case_flag = None
    
    
    @classmethod
    def set_file_path(self):
        
        """
            Sets save path, destroys set file path button, 
            then places the set url page on screen
        """
        
        self.SAVE_PATH = fd.askdirectory()
        Downloader.set_file_path_button.destroy()
        
        self.url_entry.grid(row=0, column=0, columnspan=3)
        Downloader.set_url_button.grid(row=1, column=1)


    @classmethod
    def set_url(self):
        
        """
            Destroys the set url page, gets the yt streams,
            places the ITag page on screen, places download
            button on screen
        """
        
        self.url = self.url_entry.get()
        self.url_entry.destroy()
        Downloader.set_url_button.destroy()
        
        self.yt = pytube.YouTube(self.url)
        stream_var_video = str(self.yt.streams.order_by('resolution').desc())
        stream_var_audio = str(self.yt.streams.filter(only_audio=True))
        spl_1 = stream_var_video.split(",")
        spl_2 = stream_var_audio.split(",")
        textbox_video_variable = ("\n\n".join([",".join(spl_1[i:i+1]) for i in range(0,len(spl_1),1)]))
        textbox_audio_variable = ("\n\n".join([",".join(spl_2[i:i+1]) for i in range(0,len(spl_2),1)]))
        thumb = (f'\nThumbnail url: {self.yt.thumbnail_url}\n\n')
        
        text=Text(root, width=80, height=15, borderwidth=5)
        text.insert(END, thumb)
        text.insert(END, textbox_video_variable)
        text.insert(END, '\n\n')
        text.insert(END, textbox_audio_variable)
        text.grid(row=3, column=1)
        
        Downloader.label_2.grid(row=2, column=1)
        self.itag_entry.grid(row=0, column=0, columnspan=3)
        Downloader.set_itag_button.grid(row=1, column=1)


    @classmethod
    def set_itag(self):
        
        """
            Takes ITag input, destroys ITag entry and button,
            starts downloader thread
        """
        
        try:
            self.itag_id, self.itag_id2 = map(int, self.itag_entry.get().split(','))
            self.case_flag = 1
        except ValueError:
            self.single_itag_id = self.itag_entry.get()
            self.case_flag = 0
        
        self.itag_entry.destroy()
        Downloader.set_itag_button.destroy()

        threading.Thread(target=Downloader.download, daemon=True).start()
        Downloader.label_1.grid(row=0, column=0, columnspan=3)
        Downloader.label_1.config(text=f'Working...\nClosing after complete')

    @classmethod
    def download(self):
        
        """
            Downloads the given streams,
            case 1 = 2 streams,
            case 0 = 1 stream
        """
        
        match self.case_flag:
            case 1:
                d_video_1 = self.yt.streams.get_by_itag(self.itag_id)
                d_video_2 = self.yt.streams.get_by_itag(self.itag_id2)
                video_name_1 = d_video_1.default_filename
                video_name_2 = d_video_2.default_filename
                extension_1 = os.path.splitext(video_name_1)
                extension_2 = os.path.splitext(video_name_2)
                
                name_video = f'Video_{self.yt.title}{extension_1[1]}'
                name_audio = f'Audio_{self.yt.title}{extension_2[1]}'
                
                d_video_1.download(self.SAVE_PATH, filename=name_video)
                d_video_2.download(self.SAVE_PATH, filename=name_audio)
                root.destroy()
            case 0:
                d_video = self.yt.streams.get_by_itag(self.single_itag_id)
                video_name = d_video.default_filename
                extension = os.path.splitext(video_name)
                name_file = f'File_{self.yt.title}{extension[1]}'
                d_video.download(self.SAVE_PATH, filename=name_file)
                root.destroy()


    def start_file_thread():
        threading.Thread(target=Downloader.set_file_path, daemon=True).start()
    def start_url_thread():
        threading.Thread(target=Downloader.set_url, daemon=True).start()
    def start_itag_thread():
        threading.Thread(target=Downloader.set_itag, daemon=True).start()

    
    url_entry = Entry(root, width=50, borderwidth=5)
    itag_entry = Entry(root, width=50, borderwidth=5)
    set_file_path_button = ttk.Button(root, text='Set Save Path', style='Outline.TButton', command=start_file_thread)
    set_url_button = ttk.Button(root, text='Set link', style='Outline.TButton', command=start_url_thread)
    set_itag_button = ttk.Button(root, text='Set itags and download', style='Outline.TButton', command=start_itag_thread)
    label_2 = Label(root, text="Requires one or two ITags (video, audio or either)")
    label_1 = Label(root, text=' \n')

    set_file_path_button.grid(row=1, column=1)

root.mainloop()
