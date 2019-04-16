import os
import string
import sys

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

emailCount = 0

if os.path.exists(outputFileName):
    print('The output filename exists.  Please rename it and start again.\n')
    exit()

if os.path.exists(inputFileName):
    with open(inputFileName, 'r') as fileInput:
        with open(outputFileName, 'w') as fileOutput:
            while True:
                c = fileInput.read(1)
                if not c:
                    print('End of file.')
                    print('{} email addresses extracted.'.format(emailCount))
                    break
                while c != '<':
                    c = fileInput.read(1)
                while c != '>':
                    c = fileInput.read(1)
                    if c == '>':
                        break
                    fileOutput.write(c)
                emailCount = emailCount + 1
                fileOutput.write('\n')
                #read_data = fileInput.read();


fileInput.close()
fileOutput.close()