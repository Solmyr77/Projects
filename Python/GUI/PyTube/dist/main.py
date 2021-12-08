from tkinter import ttk, END, Entry, Label, Text, Tk, filedialog as fd
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
        self.save_path = None
        self.url = None
        self.yt = None
        self.itag_id_0 = None
        self.itag_id_1 = None
        self.single_itag_id = None
        self.url_entry = None
        self.itag_entry = None
        self.case_flag = None



    class ytObject:
        
        
        def __init__(self, save_path, yt, itag, filetype):
            self.save_path = save_path
            self.yt = yt
            self.itag = itag
            self.filetype = filetype


        def download(self):
            d_video = self.yt.streams.get_by_itag(self.itag)
            video_name = d_video.default_filename
            extension = os.path.splitext(video_name)
            name_file = f'{self.filetype}_{self.yt.title}{extension[1]}'
            d_video.download(self.save_path, filename=name_file)

        
        
    @classmethod
    def set_file_path(self):
        
        
        """
            Sets save path, destroys set file path button, 
            then places the set url page on screen
        """
        
        
        self.save_path = fd.askdirectory()
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
            self.itag_id_0, self.itag_id_1 = map(int, self.itag_entry.get().split(','))
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
        

        if self.case_flag == 1:
            video = Downloader.ytObject(self.save_path, self.yt, self.itag_id_0, 'Video')
            audio = Downloader.ytObject(self.save_path, self.yt, self.itag_id_1, 'Audio')
            
            video.download()
            audio.download()
            
            root.destroy()
        elif self.case_flag == 0:
            file = Downloader.ytObject(self.save_path, self.yt, self.single_itag_id, 'File')
            file.download()
            
            root.destroy()



    def start_file_thread():
        threading.Thread(target=Downloader().set_file_path, daemon=True).start()
        
    def start_url_thread():
        threading.Thread(target=Downloader().set_url, daemon=True).start()
        
    def start_itag_thread():
        threading.Thread(target=Downloader().set_itag, daemon=True).start()

    
    
    url_entry = Entry(root, width=50, borderwidth=5)
    itag_entry = Entry(root, width=50, borderwidth=5)
    set_file_path_button = ttk.Button(root, text='Set Save Path', style='Outline.TButton', command=start_file_thread)
    set_url_button = ttk.Button(root, text='Set link', style='Outline.TButton', command=start_url_thread)
    set_itag_button = ttk.Button(root, text='Set itags and download', style='Outline.TButton', command=start_itag_thread)
    label_2 = Label(root, text="Requires one or two ITags (video, audio or either)\nTextbox is scrollable")
    label_1 = Label(root, text=' \n')

    set_file_path_button.grid(row=1, column=1)



root.mainloop()
