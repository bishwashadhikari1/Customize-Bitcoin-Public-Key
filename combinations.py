import itertools

from bitcoinaddress import Wallet

from yourword import yourword

switchablechars = ['a', 'i' , 'o', 'I', 'O']

switches = ['@', '1' , '0' , '1' , '0']

input_word = yourword

keywordset = [input_word]

newwordlist = list(input_word)

for i in range(0,len(input_word)):

    for c in switchablechars:

        if c == input_word[i]:

            newwordlist[i] = switches[switchablechars.index(c)]

            newword = ''.join(newwordlist)

            keywordset.append(newword)

current = list(input_word)


def recurrlist(current, n, input_word, keywordset):

    newwordlist = list(input_word)

    while current != newwordlist:

        for i in range(n,len(input_word)):
            for c in switchablechars:

                if c == input_word[i]:

                    newwordlist[i] = switches[switchablechars.index(c)]

                    newword = ''.join(newwordlist)

                    keywordset.append(newword) 

                    recurrlist(current, i, input_word, keywordset)

                    current = newwordlist

    return keywordset


def combinations():

    keywords = []

    wordset = recurrlist(current, 0, input_word, keywordset)

    for wooord in wordset:

        keywords += list(map(''.join, itertools.product(*zip(wooord.upper(), wooord.lower()))))

    keywords = list(set(keywords)) 

    return keywords



def trywallet(keywords):

    while True:

            wall = Wallet()

            walladdy = wall.address.__dict__['mainnet'].__dict__['pubaddr1']

            print(walladdy) # comment this line for cleaner terminal
            for word in keywords:

                if  word in walladdy :

                    f = open('privatepublickeys.txt', 'a')

                    f.write('Private key = '+ wall.key.__dict__['mainnet'].__dict__['wif'] + ' Public Key = '+  wall.address.__dict__['mainnet'].__dict__['pubaddr1'] + '\n')     

                    print('Private key = ' , wall.key.__dict__['mainnet'].__dict__['wif'])

                    print('Public key = ' , wall.address.__dict__['mainnet'].__dict__['pubaddr1'])

                    f.close()

                    break