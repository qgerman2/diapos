import time
import math
import keyboard
from datetime import datetime
from sys import exit

start = time.time()
diapos = [[1, 0]]
diapo = 1
print("Registro de diapositivas")

def nuevadiapo():
    now = math.trunc(time.time() - start)
    if diapos[-1][1] == now:
        diapos[-1][0] = diapo
    else:
        diapos.append([diapo, now])
    m, s = divmod(now, 60)
    print("Diapositiva: " + str(diapo), "Tiempo: " + str(m) + ":" + str(s).zfill(2))
        
def savediapos():
    f = open(datetime.now().strftime("%m %d %Y - %H %M %S") + ".txt", "w")
    for i,v in enumerate(diapos):
        if i==len(diapos)-1: continue
        printdiapo(v[0], str(diapos[i+1][1] - diapos[i][1]), False, f)
    printdiapo(diapos[-1][0], 1, True, f)
    f.close()
    print("Guardado")
    
def printdiapo(d, t, last, f):
    f.write("file '" + str(d) + ".png'\n")
    f.write("duration " + str(t) + "\n")
    if last:
        f.write("file '" + str(d) + ".png'")

while True:
    if keyboard.read_key() == "left":
        diapo = diapo - 1
        nuevadiapo()
    if keyboard.read_key() == "right":
        diapo = diapo + 1
        nuevadiapo()
    if keyboard.read_key() == "enter":
        savediapos()
        exit(0)