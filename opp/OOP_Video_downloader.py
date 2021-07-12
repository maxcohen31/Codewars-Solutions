from tkinter import *
from pytube import YouTube

# Initializing the main window

class Master():
    def __init__(self):
        self.main_window = Tk()
        self.title = self.main_window.title('Video downloader by maxcohen31')
        self.main_window.geometry('500x200')

        # Initializing labels
        self.label1 = Label(self.main_window, text = 'Youtube video downloader')
        self.label1.grid(row = 0, columnspan= 3, ipady = 10, sticky = N)
        self.url_link = Label(self.main_window, text = 'URL')
        self.url_link.grid(row = 1, column = 0, sticky = W)
        self.notification = Label(self.main_window)
        self.notification.grid(row = 3, columnspan = 3, pady = 10, sticky = N)
        self.saving_path = Label(self.main_window, text = 'File path')
        self.saving_path.grid(row = 2, column = 0, pady = 10, sticky = W)

        # Initializing Entry
        get_url = StringVar()
        get_path = StringVar()
        self.url_entry = Entry(self.main_window, textvariable = get_url,  width = 50)
        self.url_entry.grid(row = 1, column = 1, sticky = N)
        self.entry_path = Entry(self.main_window,textvariable = get_path, width = 50)
        self.entry_path.grid(row = 2, column = 1, pady = 10, sticky = N)

        # Initializing download button
        self.dwl_button = Button(self.main_window, text = 'Download', command = self.__getstarted)
        self.dwl_button.grid(row = 4, columnspan = 3, pady = 5, sticky = N)

    # Initializing the getstarted function
    def __getstarted(self):
        get_url = self.url_entry.get()
        get_path = self.entry_path.get()
        try:
            yt_var = YouTube(get_url)
            yt_stream = yt_var.streams.filter(progressive = True).first()
            yt_stream.download(output_path = get_path)
            self.notification.config(text = 'Video successfully downloaded')
        except Exception:
            print('Please enter URL')
            self.notification.config(text = 'Impossible to download the video')

    # Method to call the class Master
    def master_call(self):
        self.main_window.mainloop()

# Calling the class Master
if __name__ == "__main__":
    master = Master()
    master.master_call()




