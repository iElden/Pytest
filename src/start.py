from src import load
import subprocess
import sys

message = {"succes":"\x1B[92;49mSUCCES\x1B[0m",
           "fail"  :"\x1B[93;49mFAIL\x1B[0m",
           "crash" :"\x1B[91;49mCRASH\x1B[0m"}

def start():
    result = {"ok":0,"fail":0,"crash":0}
    tests = load.load()
    param = load.param()
    if param["compile"]:
        rt = subprocess.run(["make","re"])
        if rt.returncode != 0:
            print(message["crash"],"make failed")
            sys.exit(0)
    for test in tests:
        print(test.name,end=" : ")
        try :
            rt = subprocess.run([param["bin_name"],test.inp],timeout=param["timeout"])
        except TimeoutExpired:
            print(message["crash"],"\ntimeout")
            result["crash"] += 1
            continue
        if rt.returncode < 0:
            print(message["crash"],"\nLe programme à reçu le signal {} {}".format(
                str(abs(rt.returncode)),"(Segmentation Fault)" if rt.returncode == -11 else ""))
            result["crash"] += 1
        if rt.returncode != test.code:
            print(message["fail"],"\nCode attendu : {}\n Code reçu : {}"
                  .format(str(rt.returncode),str(test.code)))
            result["fail"] += 1
        elif rt.stdout != test.outpout:
            print(message["fail"],"\nAttendu : {}\nReçu : {}".format(rt.stdout,test.outpout))
            result["fail"] += 1
        else:
            print(message["succes"])
            result["ok"] += 1
    print(message["succes"],result["ok"],
          message["fail"],result["fail"],
          message["crash"],result["crash"])
