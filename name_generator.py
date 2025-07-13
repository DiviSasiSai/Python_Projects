import time
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
name = "SASI"
pname=""
j=0
i=-1

while True:
    i+=1
    if i == 26:
        i=0
    print(pname+alpha[i])
    time.sleep(0.5)
    print(CLEAR + CLEAR_AND_RETURN)
    if alpha[i] == name[j]:
        pname += alpha[i]
        j+=1
        i=-1
    if pname == name:
        break
