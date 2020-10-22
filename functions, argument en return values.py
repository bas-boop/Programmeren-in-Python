print("------------------------------------------------------------------------------")

def ree1() :
    print("reweeee")
    print("------------------------------------------------------------------------------")

ree1()

def ree2(iets) :
    print("iets is: ", iets)
    print("------------------------------------------------------------------------------")

ree2(True)

def ree3(x, y) :
    print("X is ", x, " en Y is ", y)
    print("------------------------------------------------------------------------------")

ree3(0, 1)

def ree4(aantal = 420, ietsanders = True):
    print("help", aantal)
    print("help 2", ietsanders)
    print("ta da")
    print("------------------------------------------------------------------------------")

ree4("getal")
ree4(True, False)
ree4("meer tekst")

code=69

def ree5(code):
    if(code == "69"):
        return True
    else:
        return False
ree5(69)

print(ree5(code))
#waarom is code niet 69?
