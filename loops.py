import random

isRunning = True

while (isRunning == True):
    print("herhaal!")
    if ( random.randrange(0, 69) == 1 ):
        isRunning = False
    else:
        print("Doe als laaste dit")

print("einde programma")

#         0        1   2     3
lijstA = ["tekst", 1, True, 44.05]
lijstB = ["dit", "is", "een", "reeks", "tekst"]

print(lijstA)
print(lijstA[3])

print(lijstB)
lijstB[1] = "veranders!"
print(lijstB)

#door lijst B heen gaan:
for waarde in lijstB:
    print("dit is waarde:", waarde)

lijstGrootte = len(lijstA)
print("lijstA is", lijstGrootte, "dingen lang")
print("---------------------------------------------------------")

for waarde in lijstB:
    waarde = "iets"
    print(waarde)

print(lijstB)
print("---------------------------------------------------------")

for waarde in range(5):
    print("leuk, waarde is", waarde)

for waarde in range(len( lijstB )):
    if (lijstB[waarde] == "reeks"):
        lijstB[waarde] = "reeks is verandered"
    print(lijstB[waarde])

print(lijstB)
print("---------------------------------------------------------")

objects = [ "Viool", "Bal", "Beker", "Tafel" ]
print(objects)

for index in range ( len(object)) :
    print(index)
    if ( object[ indez]  == "bal" ):
        objects [index] = ""
        break

print("bal verwijderd! (leeg gemaakt)")
print(object)

#geef het op want idk wat er fout gaat
