#------------- Boilerplate Code Start------
import socket
from tkinter import *
from  threading import Thread
from PIL import ImageTk, Image
import random

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None

playerName = None
nameEntry = None
nameWindow = None

#------------- Boilerplate Code End------


# Student write saveName() here
def saveName() :
    global SERVER
    global playerName
    global nameWindow
    global nameEntry
    playerName = nameEntry.get()
    nameEntry.delete(0 , END)
    nameWindow.destroy()
    SERVER.send(playerName.encode())
    print("details sent")



def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    global screen_width
    global screen_height

    nameWindow  = Tk()
    nameWindow.title("Tambola family fun")
   # nameWindow.attributes('-fullscreen',True)
    nameWindow.geometry('800 * 600')


    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas1 = Canvas( nameWindow, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/2, screen_height/5, text = "Enter Name", font=("Chalkboard SE",100), fill="white")

    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 50), bd=5, bg='white')
    nameEntry.place(x = screen_width/2 - 220, y=screen_height/4 + 100)

    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 30),width=15, command=saveName, height=2, bg="#80deea", bd=3)
    button.place(x = screen_width/2 - 130, y=screen_height/2 - 30)
    flashNumberLabel = canvas2.create_text(400 , screen_height/2 , text = 'Waiting for others to join...' , font = ("Chalkboard SE",30) , fill = '#3e2723')

    nameWindow.resizable(True, True)
    nameWindow.mainloop()

def recievedMsg():
    global SERVERS
    global displayNumberList
    global flashNunberLabel
globel canvas2
global gameOver
mumbers= str(i) fori in rangel(1, 91)1
while True:
chunk=SERVER. recv (2048).decode ()
if (chunk 1n nunbers and flashNumberLabel and not ganeOver) :
flashNunberList. append (int (chunk))
canvas2.itencon figure (flashNunberLabel, text - chunk, font ("Chalkboard SE", 60))
elif('wins the gane
ganeOver True
canvas2.itemconfigure (flashNumberLabel, text - chunk, font ("Chalkboard SE", 40))
in chunk):


# Boilerplate Code
def setup()
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    thread = Thread(target = recieveMessage)
    thread.start()
    

    # Creating First Window
    askPlayerName()




setup()
