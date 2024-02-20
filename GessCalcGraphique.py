
import tkinter

from tkinter import messagebox

import time

def Quitt():
  exit(1)

def Calculator():

  Db = open("DataBase.txt", "a+")

  Date = time.strftime("%A %d %B %Y a %H h %I min %S s")

  Db.write("\tGesscalc ouverte le {}\n".format(Date))

  if (StrEntered.get() == "quit" or StrEntered.get() == "QUIT" or StrEntered.get() == "Quit"):
    quit()

  OperatorPosition = StrEntered.get().find("+")

  if (OperatorPosition == -1):
    OperatorPosition = StrEntered.get().find("-")

    if (OperatorPosition == -1):
      OperatorPosition = StrEntered.get().find("*")

      if(OperatorPosition == -1):
        OperatorPosition = StrEntered.get().find("/")
  
  FirstNumber = ""

  SecondNumber = ""

  for x in range(OperatorPosition):
    FirstNumber = "{}{}".format(FirstNumber, StrEntered.get()[x])

  for x in range(OperatorPosition+1, len(StrEntered.get())):
    SecondNumber = "{}{}".format(SecondNumber, StrEntered.get()[x])

  try:
   FirstNumber = int(FirstNumber)
  except ValueError:
     messagebox.showerror("GessCalc_Error", "Le premier nombre est invalide")
  try:
   SecondNumber = int(SecondNumber)
  except ValueError:
     messagebox.showerror("GessCalc_Error", "Le deuxieme nombre est invalide")

  if (StrEntered.get()[OperatorPosition] == "+"):
    result3 = "{}+{}={}\n".format(FirstNumber, SecondNumber, FirstNumber+SecondNumber)
    messagebox.showinfo("GessCalc_Error", result3)
    Db.write("{}+{}={}\n".format(FirstNumber, SecondNumber, FirstNumber+SecondNumber))


  elif (StrEntered.get()[OperatorPosition] == "-"):
    result4 = "{}-{}={}\n".format(FirstNumber, SecondNumber, FirstNumber-SecondNumber)
    messagebox.showinfo("GessCalc_Error", result4)
    Db.write("{}-{}={}\n".format(FirstNumber, SecondNumber, FirstNumber-SecondNumber))

  elif (StrEntered.get()[OperatorPosition] == "/"):
    result5 = "{}/{}={}\n".format(FirstNumber, SecondNumber, FirstNumber/SecondNumber)
    messagebox.showinfo("GessCalc_Error", result5)
    Db.write("{}/{}={}\n".format(FirstNumber, SecondNumber, FirstNumber/SecondNumber))

  elif (StrEntered.get()[OperatorPosition] == "*"):
    result6 = "{}*{}={}\n".format(FirstNumber, SecondNumber, FirstNumber*SecondNumber)
    messagebox.showinfo("GessCalc_Error", result6)
    Db.write("{}*{}={}\n".format(FirstNumber, SecondNumber, FirstNumber*SecondNumber))

  """elif (StrEntered[OperatorPosition] == "/"):
    print("{}/{}={}\n".format(FirstNumber, SecondNumber, FirstNumber/SecondNumber))
    Db.write("{}/{}={}\n".format(FirstNumber, SecondNumber, FirstNumber/SecondNumber))"""

  """
  if("=" not in StrEntered.get()):
    Error_Message = "Soit <<{}>> est incorrect soit ce n'est pas pris en charge par GessCalc".format(StrEntered.get())
    messagebox.showerror("GessCalc_Error", Error_Message)
    #os.system("python main.py")
  """
  if ("x" in StrEntered.get() and "=" in StrEntered.get()):
    xPosition = StrEntered.get().find("x")

    a = StrEntered.get()[xPosition-1]

    if(a == "" or xPosition == 0):
      a = "1"

    OperatorPosition = StrEntered.get().find("+")

    if(OperatorPosition == -1):
      OperatorPosition = StrEntered.get().find("-")

      if(OperatorPosition == -1):
          Error_Message = "Soit <<{}>> est incorrect soit ce n'est pas pris en charge par GessCalc".format(StrEntered.get())
          messagebox.showerror("GessCalc_Error", Error_Message)
          #os.system("python main.py")

    b = StrEntered.get()[OperatorPosition+1]

    EqualPosition = StrEntered.get().find("=")

    c = StrEntered.get()[EqualPosition+1]

    try:
      a = int(a)
    except ValueError:
      messagebox.showerror("GessCalc_Error", "a est invalid")
      #os.system("python main.py")

    try:
      b = int(b)
    except ValueError:
      messagebox.showerror("GessCalc_Error", "b est invalid")
      #os.system("python main.py")

    try:
      c = int(c)
    except ValueError:
      messagebox.showerror("GessCalc_Error", "c est invalid")
      #os.system("python main.py")

    if(a == 0):
      messagebox.showerror("GessCalc_Error", "a doit etre different de 0")
      #os.system("python main.py")

    if(StrEntered.get()[OperatorPosition] == "-"):
      result1 = "X = {}".format((c+b)/a)
      messagebox.showinfo("Resultat", result1)
      Db.write("X = {}\n".format((c+b)/a))


    elif(StrEntered.get()[OperatorPosition] == "+"):
      result2 = "X = {}".format((c-b)/a)
      messagebox.showinfo("Resultat", result2)
      Db.write("X = {}\n".format((c-b)/a))

  Db.close()
  




"""
def Calculate():
    if(StrEntered.get() == "0"):
        Error_Message = "Soit <<{}>> est incorrect soit ce n'est pas pris en charge par GessCalc".format(StrEntered.get())
        messagebox.showerror("GessCalc_Error", Error_Message)
"""   
def GetStr(*args):
    StrEntered.set(entered.get())


Str = "\n\nBienvenue dans la GessCalculator \n\nFaites tous vos calculs ici\n\n"

Title = Str.center(100, "*")

window = tkinter.Tk()

window.title("GessCalc")

window.minsize(250, 250)

window.geometry("500x250+500+100")

welcome_msg = tkinter.Label(window, text=Title)

entered = tkinter.StringVar()

entry_zone = tkinter.Entry(window, width=50, textvariable=entered)

mainmenu = tkinter.Menu(window)

firstMenu = tkinter.Menu(mainmenu)
firstMenu.add_command(label="Creer un nouveau fichier")
firstMenu.add_command(label="Ouvrir un fichier")
firstMenu.add_command(label="Enregistrer")
firstMenu.add_command(label="Enregistrer sous")
firstMenu.add_command(label="Quitter", command=Quitt)

mainmenu.add_cascade(label="GessCalc Options", menu=firstMenu)





entered.trace("w", GetStr)

StrEntered = tkinter.StringVar()

Error_Message = "Soit <<{}>> est incorrect soit ce n'est pas pris en charge par GessCalc".format(StrEntered.get())








Validation_Button = tkinter.Button(window, text="Calculer", command=Calculator)


window.config(menu=mainmenu)
welcome_msg.pack(expand=1)
entry_zone.pack(expand=1)
Validation_Button.pack(expand=1)
window.mainloop()





