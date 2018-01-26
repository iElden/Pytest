import json
import os

class Tests:
    def __init__(self,inp,code,outpout,name):
        self.inp = inp
        self.code = code
        self.outpout = outpout
        self.name = name
    def return_list(self):
        if self.name:
            return([self.inp,self.code,self.outpout,self.name])
        else:
            return([self.inp,self.code,self.outpout])
        
def load():
    if not os.path.exists("tests/test.pytst"):
        print("le fichier 'tests/test.pytst' est introuvable, voulez vous le créer ?")
        while True:
            rep = input("[Yes/No] ")
            if not rep: continue
            elif rep.lower()[0] == 'y' :
                create_file()
                break
            elif rep.lower()[0] == 'n' :
                sys.exit(1)      
    tests = []
    i = 1
    with open("tests/test.pytst",'r') as file:
        for test in json.load():
            if len(test) == 3:
                name = "Test #{}".format(str(i))
            elif len(test) == 4:
                name = test[3]
            tests.append(Tests(test[0],test[1],test[2],name))
            i += 1
    return(tests)

def save(tests):
    fd = open("tests/test.pytst",'w')
    fd.write(json.dumps([test.list() for test in tests]))

def create_file():
    os.mkdir("tests")
    fd = open("tests/test.pytst",'w')
    fd.write("[]")
    print("Le fichier a été crée avec succès")
