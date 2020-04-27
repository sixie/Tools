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
    isFileEnd = False
    while not isFileEnd:
        isNewLine = False
        line = ""

        #read the next line until [stop]\n
        while not isNewLine:
            tmp = fileInput.read(6)
            if not tmp:
                isFileEnd = True
                break;
                
            if (tmp == "[stop]"):
                isNewLine = True
                tmp = fileInput.read(1) #read the line return
            else:
                #read another 10 characters and add the 6 plus 10 to the output line
                line = line + tmp
                tmp = fileInput.read(10)
                line = line + tmp
                
        #print line
        output = obj.decrypt(line)
        #print output
        fileOutput.write(output)
    

print "created decrypted output file : " + outputfilename

