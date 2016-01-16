#Zaman, M.Shehtab
#szaman5@binghamton.edu
#Lab Section: B55
#CA: Nuri Ra
#Assignment 7: Problem 1
'''

Analysis

This program encrypts and decrypts messages using the caeser cipher method. 

Output to monitor:
  operationType(str) - The type of operation (Encryption or decryption) that was
                       run
  processedMessage(str) - The encrypted or decrypted message
  
Input from keyboard:
  userInputMessage - Message to be encrypted or decrypted
  userOperation - The type of operation for the program to run
  userKeyConvertedInt - The key used for encryption or decryption

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
'''

OPERATIONS = "ed"
ENCRYPT = 1
DECRYPT = -1

# Min and limit ordinals of printable ASCII
PRINTABLE_ASCII_MIN = 31
PRINTABLE_ASCII_LIMIT = 127

#Increment for ASCII range
DELTA_MIN_LIMIT_ASCII = 95
# Allowable rotation key prefixes
KEY_PREFIX = "-"


# Functions ----------------------------------------------------------------

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
  


# Convert rotation key to value usable for requested operation
# param  op (str) - operation requested 
# param  rotationKeyStr (str)
# invoke int()
# return encryption or decryption rotation key (int)
def convertRotationKey(op, rotationKeyStr):
  if op.lower() == OPERATIONS[1]:
    rotationKeyInt = int(rotationKeyStr)*DECRYPT
  else:
    rotationKeyInt = int(rotationKeyStr)
  return rotationKeyInt
    
def operationType(opStr):
  opMessage = ""
  if opStr.lower() == OPERATIONS[0]:
    opMessage = "Encrypted"
  else:
    opMessage = "Decrypted"
  return opMessage


# Perform string modulus operation to prevent processed character 
# from going out of bounds
# param ordinal (int)
# returns adjusted ordinal of new character (int)
def keepInBounds(ordinal):
  adjustedOrdinal = ordinal

  while adjustedOrdinal < PRINTABLE_ASCII_MIN:
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


# Main -----------------------------------------------------------------------

# Gets plain text or cipher code, operation requested (encrypt or decrypt),
#   and rotation key for Caesar cipher
# Generates cipher code or plain text
def main():
  # Describe program
  print("This program encrypts or decrypts messages " + \
        "using a Caesar cipher")

  # Priming read and repeat
  userInputMessage = input("Input the message to be processed\n\
(or press <ENTER> to quit):")


  while userInputMessage:
    # Get remaining inputs, validate and convert as necessary

    userOperation = input("Do you want to encrypt or decrypt?\
      \n(Enter E for encrypt or D for decrypt):")
    
    while not operationValidated(userOperation):
      print("That operation does not appear to be valid, please try again")
      
      userOperation = input("Do you want to encrypt or decrypt?\
        \n(Enter E for encrypt or D for decrypt):")
    
    userKeyStr = input("Enter the rotation key to be used for encryption OR\
      \nthe key that was used for encryption:")
    
    while not rotationKeyValidated(userKeyStr):
      print("Invalid encryption code, please try again")
      
      userKeyStr = input("Enter the rotation key to be used for encryption OR\
      \nthe key that was used for encryption:")
    
    userKeyConvertedInt = convertRotationKey(userOperation, userKeyStr)
                           
    # Encrypt or decrypt contents of file
    processedMessage = processMessage(userInputMessage,\
                                      userKeyConvertedInt)
    # Display result
    print("The",operationType(userOperation),"message is",processedMessage)
    # Continuation read
    userInputMessage = input("Input the message to be processed\
      \n(or press <ENTER> to quit):")

main()
