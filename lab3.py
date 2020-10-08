def decryptMessage(key,message):
    keySeperater=list(key)
    messageSeperater=list(message)
    line=createLine(keySeperater)
    finalDecryptedMessage=groupDecryptedMessage(messageSeperater,line)
    return finalDecryptedMessage

def encryptMessage(key,message):
    keySeperater=list(key)
    messageSeperater=list(message)
    line=createLine(keySeperater)
    finalEncryptedMessage=groupEncryptedMessage(messageSeperater,line)
    return finalEncryptedMessage


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
                rowOfSecondLetter=5
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
        print('indexOfFirstLetter'+str(indexOfFirstLetter))
        decryptedSecondLetter=line[indexOfSecondLetter]
        messageDecrypted+=decryptedFirstLetter+decryptedSecondLetter
    return messageDecrypted
    

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
        
def createLine(keySeperater):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','v','w','x','y','z',' ']
    array=keySeperater+alphabet
    array= list(dict.fromkeys(array))
    return array

def defineRow(index):
    return int(index/5)+1

def defineColumn(index):
    return int(index%5)+1

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


