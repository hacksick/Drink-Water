
# this is a program that reminds you to drink water, no kidney stones garanteed

import os
from tkinter import *
import vact
import threading, gtts, os
from playsound import playsound
import requests, random
import shutil

chimc=os.listdir()
if("drink_icon.png" not in chimc):
    kholi = "https://www.pngitem.com/pimgs/m/407-4073680_thumb-image-drawing-bottled-water-png-transparent-png.png"
    noni = requests.get(kholi, stream=True)
    with open("drink_icon.png", 'wb') as f:
        noni.raw.decode_content = True
        shutil.copyfileobj(noni.raw, f)


root =Tk()
p1 = PhotoImage(file='drink_icon.png')
# Setting icon of master window
root.iconphoto(False, p1)
root.geometry("200x100")
root.title("Drink Water")
root.resizable(0, 0)
bg = "#212529"
astra = ["#ef233c", "#89c2d9", "#9d4edd",
         "#ff9e00", "#ffb3c1", "#78c6a3", "#be95c4", "#ffee99", "#deff0a", "#b9b5ff"]

fg = astra[random.randint(0, len(astra)-1)]
#fg = "#b9b5ff"
root.configure(bg=bg)
Label(root, text="Drink Water", font=("Trebuchet MS", 20, "bold"),
      bg=bg, fg=fg).pack()
tim = Label(root, text="", fg=fg, font=("Trebuchet MS", 20, "bold"),
      bg=bg)
tim.pack()

inter = 20
rem = "m"
zuk = 0


def say(sentence, slowly=False):
      try:
            name = "answer.mp3"
            source = gtts.gTTS(sentence, lang="en", tld="fr", slow=slowly)
            source.save(name)
            playsound("answer.mp3")
            os.remove("answer.mp3")
      except PermissionError:
            print("ERROR")


zoop=threading.Thread(target=say, args=("I will remind you to drink water every 20 minutes",))
zoop.start()
def nose():
      global rem, inter, zuk
      while True:
            
            l=vact.time()
            l=list(l.split(":"))
            h = int(l[0])
            m = int(l[1])
            s = int(l[2])
            print(h,m,s)
            if(zuk==20):
                  zuk=0
                  dam = threading.Thread(target=say,args=("please drink water",))
                  dam.start()
            if(rem == "m"):
                  rem=m
            elif(rem>m):
                  if(m==0):
                        rem=m
                        zuk+=1
            elif(rem < m):
                  rem = m
                  zuk += 1
                  
            tim.config(text="%s : %s : %s"%(h,m,s))
      
                        
dammaro = threading.Thread(target=nose)
dammaro.start()


root.mainloop()
