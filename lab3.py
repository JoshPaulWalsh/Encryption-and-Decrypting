#Joshua Walsh jpw273@nau.edu
#Adam Montano ajm2327@nau.edu

def decryptMessage(key,message):
    keySeperater=list(key)
    messageSeperater=list(message)
    line=createLine(keySeperater)
    finalDecryptedMessage=groupDecryptedMessage(messageSeperater,line)
    return finalDecryptedMessage
#This will call the key message with each value seperated into an array, it will do the same for message, it calls line in order to create the array of letters and     removes duplicates, it then proceeds to make the variable finalDecryptedMessage which is the encrypted message that they input decrypted, and it returns that variable  in order to use it in main.

def encryptMessage(key,message):
    keySeperater=list(key)
    messageSeperater=list(message)
    line=createLine(keySeperater)
    finalEncryptedMessage=groupEncryptedMessage(messageSeperater,line)
    return finalEncryptedMessage
#This will do the same as decryptMessage except the message returned is encrypted instead of decrypted

def groupDecryptedMessage(messageSeperater, line):
    index=0
    messageDecrypted=''
    while index<len(messageSeperater):
        firstLetter= messageSeperater[index]
        secondLetter= messageSeperater[index+1]
        rowOfFirstLetter=defineRow(line.index(firstLetter))
        columnOfFirstLetter=defineColumn(line.index(firstLetter))
        rowOfSecondLetter=defineRow(line.index(secondLetter))
        columnOfSecondLetter=defineColumn(line.index(secondLetter))
        if rowOfFirstLetter==rowOfSecondLetter:
            columnOfFirstLetter=columnOfFirstLetter-1
            columnOfSecondLetter=columnOfSecondLetter-1
            if columnOfFirstLetter==0:
                columnOfFirstLetter=5
            if columnOfSecondLetter==0:
                columnOfSecondLetter=5
        elif columnOfFirstLetter==columnOfSecondLetter:
            rowOfFirstLetter=rowOfFirstLetter-1
            rowOfSecondLetter=rowOfSecondLetter-1
            if rowOfFirstLetter==0:
                rowOfFirstLetter=5
            if rowOfSecondLetter==0:
                rowOfSecondLetter=5
        else: 
            firstLetterSquareColumn=columnOfSecondLetter
            secondLetterSquareColumn=columnOfFirstLetter
            columnOfFirstLetter=firstLetterSquareColumn
            columnOfSecondLetter=secondLetterSquareColumn
        indexOfFirstLetter=int((rowOfFirstLetter-1)*5+columnOfFirstLetter-1)
        indexOfSecondLetter=int((rowOfSecondLetter-1)*5+columnOfSecondLetter-1)
        index+=2
        decryptedFirstLetter=line[indexOfFirstLetter]
        decryptedSecondLetter=line[indexOfSecondLetter]
        messageDecrypted+=decryptedFirstLetter+decryptedSecondLetter
    return messageDecrypted
#The groupDecryptedMessage sorts the array into a decryptable string and decrypts the message

def groupEncryptedMessage(messageSeperater, line):
    index=0
    messageEncrypted=''
    while index<len(messageSeperater):
        firstLetter= messageSeperater[index]
        secondLetter=''
        if len(messageSeperater)%2==0 or index!=len(messageSeperater)-1:
            secondLetter= messageSeperater[index+1]
        else:
            secondLetter='x'
        if (firstLetter==secondLetter):
            messageSeperater.insert(index+1,'x')
            secondLetter=messageSeperater[index+1]
        rowOfFirstLetter=defineRow(line.index(firstLetter))
        columnOfFirstLetter=defineColumn(line.index(firstLetter))
        rowOfSecondLetter=defineRow(line.index(secondLetter))
        columnOfSecondLetter=defineColumn(line.index(secondLetter))
        if rowOfFirstLetter==rowOfSecondLetter:
            columnOfFirstLetter=columnOfFirstLetter+1
            columnOfSecondLetter=columnOfSecondLetter+1
            if columnOfFirstLetter==6:
                columnOfFirstLetter=1
            if columnOfSecondLetter==6:
                columnOfSecondLetter=1
        elif columnOfFirstLetter==columnOfSecondLetter:
            rowOfFirstLetter=rowOfFirstLetter+1
            rowOfSecondLetter=rowOfSecondLetter+1
            if rowOfFirstLetter==6:
                rowOfFirstLetter=1
            if rowOfSecondLetter==6:
                rowOfSecondLetter=1
        else: 
            firstLetterSquareColumn=columnOfSecondLetter
            secondLetterSquareColumn=columnOfFirstLetter
            columnOfFirstLetter=firstLetterSquareColumn
            columnOfSecondLetter=secondLetterSquareColumn
        indexOfFirstLetter=int((rowOfFirstLetter-1)*5+columnOfFirstLetter-1)
        indexOfSecondLetter=int((rowOfSecondLetter-1)*5+columnOfSecondLetter-1)
        index+=2
        encryptedFirstLetter=line[indexOfFirstLetter]
        encryptedSecondLetter=line[indexOfSecondLetter]
        messageEncrypted+=encryptedFirstLetter+encryptedSecondLetter
    return messageEncrypted 
#The groupEncryptedMessage does the same as the groupDecryptedMessage except for converting the array into an encrypted message

        
def createLine(keySeperater):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','v','w','x','y','z',' ']
    array=keySeperater+alphabet
    array= list(dict.fromkeys(array))
    return array
#Creates an array that resembles the box for our playfair cipher and eliminates duplicates

def defineRow(index):
    return int(index/5)+1
#defineRow function sorts the variables into hypothetical rows

def defineColumn(index):
    return int(index%5)+1
#defineColumn function sorts the variables into hypothetical columns

print('Would you like to: ')
print('(1) encrypt')
print('(2) decrypt')
shouldEncrypt=input().replace('u','v').replace('q','k')
print('Please enter a key: ')
key=input().lower()
if shouldEncrypt=='1':
    print('Please enter a message to encrypt:')
    message=input().lower().replace('u','v').replace('q','k')
    encryptedMessage=encryptMessage(key,message)
    print('Here is your encrypted message: ')
    print(encryptedMessage)
elif shouldEncrypt=='2':
    print('Please enter a message to decrypt: ')
    message=input().lower().replace('u','v').replace('q','k')
    decryptedMessage=decryptMessage(key,message)
    print('Here is your decrypted message: ')
    print(decryptedMessage)


