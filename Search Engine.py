from tkinter import *
import requests
from pywhatkit import search


import tkinter.messagebox


root = tkinter.Tk()

# root window title and dimension
root.title("GOOGLE SEARCH ")
root.geometry('500x200')

# Create a messagebox showinfo

def typesearch():
        import tkinter as tk
        from tkinter import simpledialog

        ROOT = tk.Tk()

        ROOT.withdraw()
# the input dialog
        USER_INP = simpledialog.askstring(title="type search",prompt="enter word to search:")
                                  

# check it out
        
        search(USER_INP)

def voicesearch():
	
    import speech_recognition as sr
    import webbrowser
    # It provides a high-level interface that allows displaying Web-based documents to users. 

    sr.Microphone(device_index=1)
#Take input from the mic and Convert the voice or speech to text.
    r=sr.Recognizer()
    r.energy_threshold=6000              
    # use the default microphone as the audio source
   
    with sr.Microphone() as source:
        
        audio=r.listen(source) # listen for the first phrase and extract it into audio data
        try:
            text=r.recognize_google(audio)   #recognize speech using Google Speech Recognition
            print("You said : {}".format(text))
            url='https://www.google.co.in/search?q='
            search_url=url+text
            webbrowser.open(search_url)
        except:
            print("Can't recognize")
        quit()


# Create a Buttons

Button1 = Button(root, text="typesearch", command=typesearch, pady=20)
Button2 = Button(root, text="voicesearch", command=voicesearch, pady=20)

# Set the position of buttons
Button1.place(x=50 ,y=75)
Button2.place(x=300,y=75)


root.mainloop()