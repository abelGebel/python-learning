"Programa para descargar videos desde YouTube"
from tkinter import *
from pytube import YouTube
import os
os.system('cls')

root = Tk()
root.geometry('500x300') # Tamaño del panel
root.resizable(0, 0) # Panel estatico
root.title('Doownload') # Titulo del panel
root.configure(bg='#AACDE2') # Color del fondo 

Label(root, text='Descarga tus videos', font='arial 20 bold', 
      bg='#AACDE2').place(x=90, y=30)

link = StringVar()
Label(root, text='Link:', font='arial 12', bg='#AACDE2').place(x=200, y=90)

link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=120)

current_directory = os.getcwd()
output_path = current_directory

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download(output_path=output_path)
    Label(root, text='DESCARGADO', font='arial 13 bold', 
            bg='#AACDE2', fg='#B57199').place(x=180, y=240)
    
Button(root, text='Descargar', font='arial 13 bold italic',
       bg='#B57199', padx=2, command=Downloader).place(x=180, y=180)

root.mainloop()
