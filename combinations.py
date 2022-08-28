import itertools

from bitcoinaddress import Wallet 

from yourword import yourword

switchablechars = ['a', 'i' , 'o', 'I', 'O'] # mutant conversion keys

switches = ['@', '1' , '0' , '1' , '0'] #mutant conversion values

input_word = yourword 

keywordset = [input_word] # initializing the list of keywords

newwordlist = list(input_word) # split the word into char list

for i in range(0,len(input_word)): # for individual letters of the word

    for c in switchablechars: # loop through switchable letters

        if c == input_word[i]: # if certain word is replaceable

            newwordlist[i] = switches[switchablechars.index(c)] # changing the new word's index'th letter to the corresponding mutant

            newword = ''.join(newwordlist) # converting char list back to string
 
            keywordset.append(newword) # adding the newly formed string to possible keywords list

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

    keywords = [] # initializing list to store all possible keywords

    wordset = recurrlist(current, 0, input_word, keywordset) # recursive function call that returns list of possible keywords with mutants

    for wooord in wordset: # looping through all the keywords

        keywords += list(map(''.join, itertools.product(*zip(wooord.upper(), wooord.lower())))) # adding all combinations of Uppercase and Lower case of the keyword (permutations)

    keywords = list(set(keywords))  # removing duplicates

    return keywords # returns all possible keywords



def trywallet(keywords):
    # basic DDOS function that checks for the keyword in a wallet public key

    while True: # infinite loop

            wall = Wallet() # new instance of wallet leveraging the package bitcoinaddress

            walladdy = wall.address.__dict__['mainnet'].__dict__['pubaddr1'] # extract public key from the wallet

            print(walladdy) # comment this line for cleaner terminal
            for word in keywords: # loop through all the keywords

                if  word in walladdy : # if keyword/mutants is present in the public key

                    f = open('privatepublickeys.txt', 'a') # opens the file in append mode to write from the last line 

                    f.write('Private key = '+ wall.key.__dict__['mainnet'].__dict__['wif'] + ' Public Key = '+  wall.address.__dict__['mainnet'].__dict__['pubaddr1'] + '\n') # write both private and public keys in the file  

                    f.close() # closes file instance

                    break # breaks the for loop