import sys
from Crypto.Cipher import AES

if len(sys.argv) < 4:
    print "Usage: encrypt.py [InputFileName] [OutputFileName] [keyString]"
    exit()

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

fillerCharacter = "q"
inputkey = sys.argv[3]
key = ""
if (len(inputkey) <= 16):    
    key = inputkey + fillerCharacter*(16-len(inputkey))
elif (len(inputkey) <= 24):
    key = inputkey + fillerCharacter*(24-len(inputkey))
elif (len(inputkey) <= 32):
    key = inputkey + fillerCharacter*(32-len(inputkey))

else:
    print "Error: your key " + key + " is too long. It must be less than 32 characters.\n"
    exit()


obj = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    
fileInput = open(inputfilename, 'r')
fileOutput = open(outputfilename, 'w')

with open(inputfilename, 'r') as fileInput:
    while (True):
        line = fileInput.read(17)
        #print line
        if not line:
            break
        else:
            output = obj.decrypt(line[:-1])
            #print output
            fileOutput.write(output)
    

print "created decrypted output file : " + outputfilename

