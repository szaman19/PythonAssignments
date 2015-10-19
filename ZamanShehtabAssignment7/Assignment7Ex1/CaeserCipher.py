OPERATIONS = "ed"
ENCRYPT = 1
DECRYPT = -1

# Min and limit ordinals of printable ASCII
PRINTABLE_ASCII_MIN = 31
PRINTABLE_ASCII_LIMIT = 127

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
    adjustedOrdinal = adjustedOrdinal + 95

  while adjustedOrdinal > PRINTABLE_ASCII_LIMIT-1:
    adjustedOrdinal -= 95

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