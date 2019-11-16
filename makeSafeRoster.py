import os
import string
import sys
import io
import re

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

firstRow = 'username,first name,last name,attendee email,attended,attendee company'

emailCount = 0

if os.path.exists(outputFileName):
    print('The output filename exists.  Please rename it and start again.\n')
    exit()

if os.path.exists(inputFileName):
    with open(inputFileName, 'r') as fileInput,   \
         open(outputFileName, 'w') as fileOutput:

            if firstRow != '':
              fileOutput.write(firstRow)
              fileOutput.write('\n')

            for inputLine in fileInput:
              
              nameList = re.split(";", inputLine)   
               
              for nameEntry in nameList:
                  #print('\n Name: ', nameEntry)
                  email = re.search('<.+?>', nameEntry)
                  if email:
                    email = email.group(0)[1:-1]
                    #print('Email: ', email)
                  else: email = ''
                  lastName  = re.search('\w+,', nameEntry)
                  if lastName:
                    lastName = lastName.group(0)[:-1]
                    #print('Last Name: ', lastName)
                  else: lastName = ''
                  firstName = re.search(',\s\w+', nameEntry)
                  if firstName:
                    firstName = firstName.group(0)[2:]
                    #print('First Name: ', firstName)
                  else: firstName = ''

                  if email != '':
                    emailCount = emailCount + 1
                    csvLine = email + ',' + lastName + ',' + firstName + ',' + email
                    csvLine = csvLine + ',+,Memorial Sloan Kettering Cancer Center\n'
                    fileOutput.write(csvLine)
                    print(csvLine)

            print('End of file.')
            print('{} email addresses extracted.'.format(emailCount))


fileInput.close()
fileOutput.close()