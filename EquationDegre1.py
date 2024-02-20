
while True:
        
    Equation = input(">>")

    if (Equation == "quit" or Equation == "QUIT" or Equation == "Quit"):
        exit(0)


    xPosition = Equation.find("x")

    a = Equation[xPosition-1]

    if(a == "" or xPosition == 0):
        a = "1"

    OperatorPosition = Equation.find("+")

    if(OperatorPosition == -1):
        OperatorPosition = Equation.find("-")

        if(OperatorPosition == -1):
            print("Equation incorrect")
            continue

    b = Equation[OperatorPosition+1]

    EqualPosition = Equation.find("=")

    c = Equation[EqualPosition+1]

    try:
        a = int(a)
    except ValueError:
        print("a est invalide")
        continue

    try:
        b = int(b)
    except ValueError:
        print("b est invalide")
        continue

    try:
        c = int(c)
    except ValueError:
        print("c est invalide")
        continue

    if(a == 0):
        print("a doit etre different de 0")
        continue

    if(Equation[OperatorPosition] == "-"):
        print("X = {}".format((c+b)/a))
    elif(Equation[OperatorPosition] == "+"):
        print("X = {}".format((c-b)/a))
























































































