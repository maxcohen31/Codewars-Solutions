from tkinter import *
from pytube import YouTube

# Initializing the main window
main_window = Tk()
main_window.title('Video downloader by maxcohen31')

# Initializing the function to run the button
def getstarted():
    url = get_url.get()
    try:
        yt_var = YouTube(url)
        yt_var.streams.first().download('../../Video')
        notification.config(text = 'Video successfully downloaded!')
    except Exception:
        print('Error, please insert URL')
        notification.config(text = 'Impossible to download the video')

# Initializing Label
main_window_lab = Label(main_window, text = 'Youtube Video Downloader')
main_window_lab.grid(row = 0, columnspan = 3, pady = 5, sticky = N)
notification = Label(main_window)
notification.grid(row = 4, columnspan = 3, pady = 10, sticky = N)

# Initializing Entry
get_url = StringVar()
entry_box = Entry(main_window, textvariable = get_url, width = 50)
entry_box.grid(row = 2, columnspan = 3, pady = 5)

# Initializing the main button
main_button = Button(main_window, text = "Download", command = getstarted)
main_button.grid(row = 5, columnspan  = 3, padx = 20, pady = 5, sticky = S)

main_window.mainloop()
