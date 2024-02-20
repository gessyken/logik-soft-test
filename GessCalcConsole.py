
#This is a small console calcalator devolopped by GESSY KEN ...

"""

My calculator take a string from the user and divid it into to part between the operator
and after it cast every part to integer and make the operation

"""

import os

import time



def FirstDegreeEquation():

  if (StrEntered == "quit" or StrEntered == "QUIT" or StrEntered == "Quit"):
    quit()

  if("=" not in StrEntered):
    print("Equation incorrecte")
    os.system("python main.py")

  xPosition = StrEntered.find("x")

  a = StrEntered[xPosition-1]

  if(a == "" or xPosition == 0):
     a = "1"

  OperatorPosition = StrEntered.find("+")

  if(OperatorPosition == -1):
    OperatorPosition = StrEntered.find("-")

    if(OperatorPosition == -1):
      print("Calcul incorrect")
      os.system("python main.py")

  b = StrEntered[OperatorPosition+1]

  EqualPosition = StrEntered.find("=")

  c = StrEntered[EqualPosition+1]

  try:
    a = int(a)
  except ValueError:
    print("a est invalide")
    os.system("python main.py")

  try:
    b = int(b)
  except ValueError:
    print("b est invalide")
    os.system("python main.py")

  try:
    c = int(c)
  except ValueError:
    print("c est invalide")
    os.system("python main.py")

  if(a == 0):
    print("a doit etre different de 0")
    os.system("python main.py")

  if(StrEntered[OperatorPosition] == "-"):
    print("X = {}".format((c+b)/a))
    Db.write("X = {}\n".format((c+b)/a))

  elif(StrEntered[OperatorPosition] == "+"):
    print("X = {}".format((c-b)/a))
    Db.write("X = {}\n".format((c-b)/a))


Date = time.strftime("%A %d %B %Y a %H h %I min %S s")

File = open("DataBase.txt", "a+")

File.write("\tGesscalc ouverte le {}\n".format(Date))

File.close()

State = True

Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

Str = "Bienvenue dans le GessCalc... Faites tous vos Calculs ici"

Title = Str.center(100, "-")

print("{}\n\n".format(Title))

iterations = 0
  
while State:

  Db = open("DataBase.txt", "a+")

  iterations+=1

  if(iterations == 10):
    iterations = 0
    print("Une seconde, la console va etre nettoyee\n")
    time.sleep(3)
    os.system("cls")
    

  StrEntered = input(">>")

  """
  while(StrEntered not in Refused and len(StrEntered) < 3):
    StrEntered = input("Veuillez entrer un StrEntered valid svp...\n")
  """


  if (StrEntered == "quit" or StrEntered == "QUIT" or StrEntered == "Quit"):
    os.system("cls")
    for i in range(5):
          print("Bye bye ...\n\t")
          time.sleep(1)
    exit(0)

  if("x" in StrEntered):
    FirstDegreeEquation()
    continue

  OperatorPosition = StrEntered.find("+")

  if (OperatorPosition == -1):
    OperatorPosition = StrEntered.find("-")

    if (OperatorPosition == -1):
      OperatorPosition = StrEntered.find("*")

      if(OperatorPosition == -1):
        OperatorPosition = StrEntered.find("/")
  
  FirstNumber = ""

  SecondNumber = ""

  for x in range(OperatorPosition):
    FirstNumber = "{}{}".format(FirstNumber, StrEntered[x])

  for x in range(OperatorPosition+1, len(StrEntered)):
    SecondNumber = "{}{}".format(SecondNumber, StrEntered[x])

  try:
   FirstNumber = int(FirstNumber)
  except ValueError:
    print("Le premier nombre est incorrect\n\tVeuillez entrer un nombre valide")
    continue

  try:
   SecondNumber = int(SecondNumber)
  except ValueError:
    print("Le second nombre est incorrect\n\tVeuillez entrer un nombre valide")
    continue

  if (StrEntered[OperatorPosition] == "+"):
    print("{}+{}={}\n".format(FirstNumber, SecondNumber, FirstNumber+SecondNumber))
    Db.write("{}+{}={}\n".format(FirstNumber, SecondNumber, FirstNumber+SecondNumber))


  elif (StrEntered[OperatorPosition] == "-"):
    print("{}-{}={}\n".format(FirstNumber, SecondNumber, FirstNumber-SecondNumber))
    Db.write("{}-{}={}\n".format(FirstNumber, SecondNumber, FirstNumber-SecondNumber))

  elif (StrEntered[OperatorPosition] == "+"):
    print("{}/{}={}\n".format(FirstNumber, SecondNumber, FirstNumber/SecondNumber))
    Db.write("{}/{}={}\n".format(FirstNumber, SecondNumber, FirstNumber/SecondNumber))

  elif (StrEntered[OperatorPosition] == "*"):
    print("{}*{}={}\n".format(FirstNumber, SecondNumber, FirstNumber*SecondNumber))
    Db.write("{}*{}={}\n".format(FirstNumber, SecondNumber, FirstNumber*SecondNumber))

  elif (StrEntered[OperatorPosition] == "/"):
    print("{}/{}={}\n".format(FirstNumber, SecondNumber, FirstNumber/SecondNumber))
    Db.write("{}/{}={}\n".format(FirstNumber, SecondNumber, FirstNumber/SecondNumber))

  Db.close()
  
