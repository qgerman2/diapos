import sys
import os

if len(sys.argv) < 2:
    print("sin entrada")
    sys.exit(0)
    
time = 0
filename, extension = os.path.splitext(sys.argv[1])
outputFilename = filename
if filename.find("_mu") != -1:
    outputFilename = filename[0:filename.find("_mu")] + "_ts.txt"
else:
    outputFilename = filename + "_ts.txt"

f_input = open(filename + extension, "r")
f_output = open(outputFilename, "w")
for l in f_input.readlines():
    if l.find("file") != -1:
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        image = l[6:l.find("'", 6)]
        result = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2) + "/" + image
        print(result)
        f_output.write(result + "\n")
    else:
        time = time + int(l[9:-1])
f_input.close()
f_output.close()