print('Would you like to: ')
print('(1) encrypt')
print('(2) decrypt')
shouldEncrypt=input()
print('Please enter a key: ')+key=input()
if shouldEncrypt=='1':
    print('Please enter a message to encrypt:')
    message=input()
    encryptedMessage=encryptMessage(key,message)
    print('Here is your encrypted message: ')
    print(encryptedMessage)
elif shouldEncrypt=='2':
    print('Please enter a message to decrypt: ')
    message=input()
    decryptedMessage=decryptMessage(key,message)
    print('Here is your decrypted message: ')
    print(decryptedMessage)

def decryptMessage(key,message):

def encryptMessage(key,message):
    keySeperater=list(key)
    messageSeperater=list(message)
    line=createLine(keySeperater)
    groupMessage(messageSeperater,line)

def groupMessage(messageSeperater,line)
    index=0
    while index<len(messageSeperater):
        firstLetter= messageSeperater[index]
        secondLetter=''
        if len(messageSeperater)%2==0 or index!=len(messageSeperater)-1:
            secondLetter= messageSeperater[index+1]
        else:
            secondLetter='X'
        rowOfFirstLetter=defineRow(firstLetter)
        columnOfFirstLetter=defineColumn(firstLetter)
        rowOfSecondLetter=defineRow(secondLetter)
        columnOfSecondLetter=defineColumn(secondLetter)
        if rowOfFirstLetter==rowOfSecondLetter:
            columnOfFirstLetter=columnOfFirstLetter+1
            columnOfSecondLetter=columnOfSecondLetter+1
            if columnOfSecondLetter=6:
                columnOfFirstLetter=1
                rowOfSecondLetter=rowOfSecondLetter+1
                if rowOfSecondLetter=6:
                    rowOfSecondLetter=1
        if columnOfFirstLetter==columnOfSecondLetter:
            rowOfFirstLetter=rowOfFirstLetter+1
            rowOfSecondLetter=rowOfSecondLetter+1
            if rowOfSecondLetter==6:
                rowOfSecondLetter=1
                columnOfSecondLetter=columnOfFirstLetter+1
                if columnOfSecondLetter=6:
                    columnOfSecondLetter=1
        else: 
            firstLetterSquareColumn=columnOfSecondLetter
            secondLetterSquareColumn=columnOfFirstLetter
            columnOfFirstLetter=firstLetterSquareColumn
            columnOfSecondLetter=secondLetterSquareColumn
        messageString=((rowOfFirstLetter-1)*5+columnOfFirstLetter=indexOfFirstLetter-1,(rowOfSecondLetter-1)*5+columnOfSecondLetter=indexOfSecondLetter-1)
        index+=2
    
def createLine(keySeperater):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','v','w','x','y','z',' ']
    array=keySeperater+alphabet
    array= list(dict.fromkeys(array))
    return array

def defineRow(index):
    return index/5

def defineColumn(index):
    return index%5
