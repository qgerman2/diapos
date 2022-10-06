import sys
import os

if len(sys.argv) < 2:
    print("sin entrada")
    sys.exit(0)
    
lastTime = 0
filename, extension = os.path.splitext(sys.argv[1])
outputFilename = filename
if filename.find("_ts") != -1:
    outputFilename = filename[0:filename.find("_ts")] + "_mu.txt"
else:
    outputFilename = filename + "_mu.txt"
    
f_input = open(filename + extension, "r")
f_output = open(outputFilename, "w")
for i, l in enumerate(f_input.readlines()):
    h = int(l[0:2])
    m = int(l[3:5])
    s = int(l[6:8])
    file = l[9:-1]
    time = h*60*60 + m*60 + s
    delta = time - lastTime
    lastTime = time
    if i > 0:
        res1 = "duration " + str(delta)
        f_output.write(res1 + "\n")
        print(res1)
    res2 = "file '" + file + "'"
    f_output.write(res2 + "\n")
    print(res2)
f_input.close()
f_output.close()