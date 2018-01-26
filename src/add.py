from src import load

def add(argv):
    tests = load.load()
    if len(argv) <= 2:
        inp = input_inp()
    else:
        inp = int(argv[2])
    if len(argv) <= 3:
        code = input_code()
    else:
        code = int(argv[3])
    if len(argv) <= 4:
        outpout = input("Quelle est la sortie attendu >")
    else:
        outpout = argv[4]
    if len(argv) > 5:
        name = argv[5  ]
    else:
        name = input_name()
    if name:
        tests.append([inp,code,outpout,name])
    else:
        tests.append([inp,code,outpout])
    save(tests)

def input_inp():
    print("Input du test :")
    return(input("> "))

def input_code():
    print("Entrez le code retour attendu (par défaut 0) :")
    code = input("> ")
    if not code:
        code = 0
    return(int(code))

def input_outp():
    print("Sortie attendu (Laissez vide pour tester uniquement le code retour) :")
    return(input("> "))

def input_name():
    print("Quelle est le nom du test (optionnel)")
    return(input("> "))