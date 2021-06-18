# This project is an application to download the youtube songs on device

# Importing libraries 
from tkinter import *
from pytube import YouTube
# creating display window
window = Tk()
window.geometry('500x300')
window.resizable(0,0)
window.title("Youtube video downloader app")
# creating lable
Label(window,text = 'Youtube Video Downloader Application', font ='arial 15 bold', fg = 'red').pack(pady = 10)
# creating field to enter link
link = StringVar()

Label(window, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(window, width = 70,textvariable = link).place(x = 32, y = 90)
# creating field to start downloading
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(window, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(window,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

window.mainloop()
