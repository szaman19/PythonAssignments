#Zaman, M.Shehtab
#szaman5@binghamton.edu
#Lab Section: B55
#CA: Nuri Ra
#Assignment 10: Problem 1
'''

Analysis

This program encrypts and decrypts messages using the caeser cipher method
and outputs it to a file. 

Output to monitor:
  prettyStringsFilesInDirectory(list) - Prints a list of files in the directory.
  processedMessage(str) - The encrypted or decrypted message
  
Input from keyboard:
  openFileName(str) - File name to be encrypted or decrypted
  userOperation(str) - The type of operation for the program to run
  userKeyConverted(int) - The key used for encryption or decryption

Tasks allocated to Functions:
  operationValidated(opStr) - validates whether opStr from user is valid
  rotationKeyValidated(rotationKeyStr) - validates whetehr rotationKeyStr 
    is valid
  convertRotationKey(op,rotationKeyStr) - Converts rotationKeyStr according 
    to the operation provied in op
  operationType(opStr) - takes shorthand operation type and returns the 
    complete word
  keepInBounds(ordinal): takes ordinal and loops until ordinal is 
     PRINTABLE_ASCII_MIN<ordinal<PRINTABLE_ASCII_LIMIT
  processMessage(message, rotationKey) - encrypts the message using rotation
    key and calling keepInBounds()
  writeToFile(fileObject, texLinesList) - Writes lines of strings on to a file.
  makeName(fileName,operation,rotationKey) - Creates a name for the file using 
    naming conventions and the operation and the rotation key.
  prettyStringsFilesInDirectory(): - Creates a list of directories
  fileNameValidated(name) - Checks wheteher the file exists in the directory  
'''
import os.path

# Mapping of valid operations to rotationKey factor
OPERATIONS = {'e':[1,"Encrypted"], 'd':[-1,"Decrypted"]}

# Min and limit ordinals of printable ASCII
PRINTABLE_ASCII_MIN = 32
PRINTABLE_ASCII_LIMIT = 127

#Increment for ASCII range
DELTA_MIN_LIMIT_ASCII = 95

# Allowable rotationKey prefixes
KEY_PREFIX = "-"

# Required file extension
FILE_EXT = ".txt"

# File processing modes
READ_MODE = 'r'
WRITE_MODE = 'w'

# Functions ----------------------------------------------------------------


# Checks that file exists and that extension is .txt
# param name (str) - file name
# invoke isFile() from module os.path and endswith()
# return True when valid, False otherwise (bool)
def fileNameValidated(name):
  return os.path.isfile(name) and name.endswith(FILE_EXT)

def prettyStringsFilesInDirectory():
  directoryListing = "The available files in the current directory are: \n"
  fileCounter = 1
  for eachFile in os.listdir(os.curdir):
    if eachFile.endswith(FILE_EXT):
      directoryListing += str(fileCounter)+") "+eachFile+"\n"
      fileCounter +=1
  return directoryListing 

# Generates output file name from input file name, 
#   operation requested and rotation key
# param fileName (str) - input file name
# param operation (str)
# param rotationKey (int) - converted key
# invoke str.split(), str.replace() and str.join()
# return output file name (str)
def makeName(fileName, operation, rotationKey):
  nameList = fileName.split(".")
  nameList[0] = nameList[0].replace(OPERATIONS['e'][1], "")
  nameList[0] = nameList[0].replace(OPERATIONS['d'][1], "")
  nameList[0] += (OPERATIONS[operation.lower()][1] + str(rotationKey))
  return ".".join(nameList)

# Check that requested operation is valid
# param opStr (str) - operation requested
# invoke len()
# invoke str.lower()
# return  True when valid, False otherwise (bool)
def operationValidated(opStr):
  return len(opStr) == 1 and opStr.lower() in OPERATIONS


# Check that rotation key is of form <digits> or -<digits>
# param rotationKeyStr (str)
# invoke str.isdigit() 
# returns:  True when valid, False otherwise (bool)
def rotationKeyValidated(rotationKeyStr):
  return rotationKeyStr.isdigit() or (rotationKeyStr[0]==KEY_PREFIX and \
    rotationKeyStr[1:].isdigit())

# Perform string modulus operation to prevent processed character 
# from going out of bounds
# param ordinal (int)
# returns adjusted ordinal of new character (int)
def keepInBounds(ordinal):
  adjustedOrdinal = ordinal

  while adjustedOrdinal < PRINTABLE_ASCII_MIN-1:
    adjustedOrdinal = adjustedOrdinal + DELTA_MIN_LIMIT_ASCII

  while adjustedOrdinal > PRINTABLE_ASCII_LIMIT-1:
    adjustedOrdinal -= DELTA_MIN_LIMIT_ASCII

  return adjustedOrdinal

# Encrypt or decrypt message using rotationKey
# param message (str)
# param rotationKey (int)
# invoke keepInBounds()    
# return processedMessage (str)  
def processMessage(message, rotationKey):
  result = ""

  for char in message:
    #print(keepInBounds(ord(char)+rotationKey))
    #print(chr(keepInBounds(ord(char)+rotationKey)))  
    result = result + chr(keepInBounds(ord(char)+rotationKey))

  return result

# Convert rotation key to value usable for requested operation
# param  op (str) - operation requested 
# param  rotationKeyStr (str)
# invoke int()
# return encryption or decryption rotation key (int)
def convertRotationKey(op, rotationKeyStr):
  return int(rotationKeyStr)*OPERATIONS[op.lower()][0]

# Writes encrypted lines of text onto a given file
# param fileObject 
# param texLinesList - List of encrypted strings
# return nothing - written directly to file
def writeToFile(fileObject, textLinesList):
  for eachLine in textLinesList:
    fileObject.write(eachLine+"\n")

def main():
  print(prettyStringsFilesInDirectory())
  openFileName= input("Please enter a text file or <Enter> to quit: ")
  

  while openFileName:
    try:
      openedFile = open(openFileName,READ_MODE)

      try:
        lines = openedFile.readlines()
        
        encryptedLines = []

        userOperation = input("Do you want to encrypt or decrypt?\
          \n(Enter E for encrypt or D for decrypt):")
        
        while not operationValidated(userOperation):
          print("That operation does not appear to be valid,\
           please try again")
          
          userOperation = input("Do you want to encrypt or decrypt?\
            \n(Enter E for encrypt or D for decrypt):")
        
        userKeyStr = input("Enter the rotation key to be used for encryption\
         OR \nthe key that was used for encryption:")
        
        while not rotationKeyValidated(userKeyStr):
          print("Invalid encryption code, please try again")
          
          userKeyStr = input("Enter the rotation key to be \
            used for encryption OR nthe key that was used for encryption:")
        
        userKeyConvertedInt = convertRotationKey(userOperation, userKeyStr)
        print(userKeyConvertedInt)
        for eachLine in lines:
          encryptedLines.append(processMessage(eachLine[:-1],\
            userKeyConvertedInt))
        try:
          newFile = open(makeName(openFileName,userOperation,userKeyStr),\
            WRITE_MODE)
          #writeToFile(newFile,encryptedLines)
          
          try:
            writeToFile(newFile,encryptedLines)
          
          except IOError as err: 
          # inner exception handler for outfile processing
            print("\nProblem writing data: \n" + str(err))
          except TypeError as err:  
          # inner exception handler for outfile processing
            print("\nProblem writing data, wrong format or corrupted?  \n" \
              + str(err) + '\n')
          except Exception as err: 
          # inner exception handler for outfile processing
            print("\nData cannot be written to file: \n" + str(err) + '\n')
          finally:
          # will close file whether or not exception has been raised
            newFile.close()
            print("new file",makeName(openFileName,userOperation,userKeyStr)\
              ,'created')
        
        except IOError as err: 
        # "outer" exception handler for outfile open
          print("\nExecption raised during open of output file,\
           no write performed: \n" + str(err) + '\n')
        except Exception as err: 
        # outer exception handler for outfile processing
          print("\nData cannot be read:  \n" + str(err) + '\n')  

      except IOError as err: 
      # inner exception handler for infile processing
        print("\nProblem reading data: \n" + str(err))
      except ValueError as err: 
      # inner exception handler for infile processing
        print("\nProblem processing data, wrong format or corrupted? \n"\
         + str(err) + '\n')
      except Exception as err: 
      # inner exception handler for infile processing
        print("\nData cannot be read:  \n" + str(err) + '\n')        
      finally:
      # will close file whether or not exception has been raised
        openedFile.close()
        print(openFileName,"read")

    except FileNotFoundError as err:  
    # outer exception handler for infile open
      print("\nFile not found:  deleted or in wrong folder?  \n" \
        + str(err) + '\n')
    except IOError as err: 
    # outer exception handler for infile open
      print("\nException raised during open of input file, \
        try a different file: \n" + str(err) + '\n')
    except Exception as err: 
    # outer exception handler for infile open
      print("\nData cannot be read:  \n" + str(err) + '\n')
    print(prettyStringsFilesInDirectory())
    openFileName= input("Please enter a text file or <Enter> to quit: ")
  
  
  
main()



