import itertools

infile =  "infile.txt"
keyfile = "keyfile.txt"
outfile = "outfile.txt"

def getintext():
    with open(infile, 'r') as file:
        return file.read()	#read all until EOF

def writetext(outtext):
    with open(outfile, 'w') as file:
        file.write(outtext)	#read all until EOF

def getkey(keyfile):
    with open("keyfile.txt", 'r') as keyfile:
        return keyfile.read()


def caesar(intext, key, decode=False):
    if decode:
        decode_multiplier = -1          #decode instead of encoding
    else:
        decode_multiplier = 1
    intext = intext.upper()
    cyclic_key = itertools.cycle(key)
    length = ord("Z") - ord("A")
    outlist = []
    for c in intext:
        if ord(c) >= ord("A") and ord(c) <= ord("Z"):
            outlist.append(
                chr(  (ord(c) - ord("A") + ord(cyclic_key.__next__()) * decode_multiplier) % length + ord("A")  )   
                          )
    return "".join(outlist)





if __name__ == "__main__":
    intext = getintext()
    key    = getkey(keyfile)
    outtext = caesar(intext, key)
    writetext(outtext)