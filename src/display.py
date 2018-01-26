from src import load

def display():
    for test in load.load():
        if test.name : print(test.name + " :")
        print("    code retour : {}".format(str(test.code)))
        print("    sortie      : {}".format(test.outpout))
        print('\n')
