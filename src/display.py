from src import load

def display():
    for test in load.load():
        if test.name : print(test.name + " :")
        print("    entrée : {}".format(test.inp))
        print("    code   : {}".format(str(test.code)))
        print("    sortie : {}".format(test.outpout))
        print("")
