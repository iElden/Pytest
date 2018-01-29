import json
import os
import sys
import traceback

class Tests:
    def __init__(self,inp,code,outpout,name):
        outpout = outpout.replace("\\n","\n")
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
            rep = input("[Yes/No] > ")
            if not rep: continue
            elif rep.lower()[0] == 'y' :
                create_file()
                return([])
            elif rep.lower()[0] == 'n' :
                sys.exit(1)      
    tests = []
    try:
        i = 1
        with open("tests/test.pytst",'r') as file:
            for test in json.load(file):
                if len(test) == 3:
                    name = "Test #{}".format(str(i))
                elif len(test) == 4:
                    name = test[3]
                tests.append(Tests(test[0],test[1],test[2],name))
                i += 1
    except Exception:
        with open("tests/test.pytst",'r') as file:
            if file.read() == "[]" : return([])
        print("FATAL ERROR : Le fichier de sauvegarde des tests est conrompue !")
        print("essayez de modifier tests/test.pytst ou de le supprimer")
        traceback.print_exc()
        sys.exit(2)
    return(tests)

def save(tests):
    fd = open("tests/test.pytst",'w')
    fd.write(json.dumps([test.return_list() for test in tests],indent="  "))
    fd.close()
    
def create_file():
    os.mkdir("tests")
    fd = open("tests/test.pytst",'w')
    fd.write("[]")
    fd.close()
    print("Le fichier a été crée avec succès")

def param():
    if not os.path.exists("tests/param.pytst"):
        print("le fichier 'tests/param.pytst' est introuvable, voulez vous le créer ?")
        while True:
            rep = input("[Yes/No] > ")
            if not rep: continue
            elif rep.lower()[0] == 'y' :
                fd = open("tests/param.pytst",'w')
                bn = input("Quelle est le nom du binaire ?\n> ")
                dico = {"bin_name":bn,"timeout":5,"compile":True}
                fd.write(json.dumps(dico))
                fd.close
                return(dico)
            elif rep.lower()[0] == 'n' :
                sys.exit(1)
    fd = open("tests/param.pytst",'r')
    dic = json.load(fd)
    fd.close()
    return(dic)
