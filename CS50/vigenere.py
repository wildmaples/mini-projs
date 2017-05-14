##################
## CS50 PSET 6 - vigenere.py 
## vigenere.py encrypts messages using Vigenère’s cipher
##################

import sys
import string

## Exit if there aren't two sys.arguments
if len(sys.argv) != 2:
    sys.exit("Error: Two arguments only.")

## Exit if argument entered is not alphabets
if not str.isalpha(sys.argv[1]):
    sys.exit("Error: Alphabetic values only.")

## Defining variables 
key_length = len(sys.argv[1])
keyword = sys.argv[1]

## Ask for plaintext and print ciphertext
plaintext = input("plaintext: ")
print ("ciphertext: ", end="")

length = len(plaintext)
i = 0
k = 0

## Iterate over plaintext length
for i in range (length):
    loop = k % key_length
    
    ## Check if it is a number or space, reprord
    if not str.isalpha(plaintext[i]) or str.isspace(plaintext[i]):
        print(plaintext[i], end="")
        i+=1
        
    ## Else if not number or space,
    ## check if key is upper or lower case,
    
    ## If key is upper case
    elif str.isupper(keyword[loop]):
        
        ## check if plaintext is upper
        if str.isupper(plaintext[i]):
            ascii_num = ord(plaintext[i])
            out = ((((ascii_num-ord("A")) + ((ord(keyword[loop])-ord("A")))) % 26) + ord("A"))
            print(chr(out), end="")
            k+=1
            i+=1
        
        ## check if plaintext is lower
        elif str.islower(plaintext[i]):
            ascii_num = ord(plaintext[i])
            out = ((((ascii_num-ord("a")) + ((ord(keyword[loop])-ord("A")))) % 26) + ord("a"))
            print(chr(out), end="")
            k+=1
            i+=1
    
    ## Else if key is lower case
    elif str.islower(keyword[loop]):
        
        ## Check if plaintext is upper
        if str.isupper(plaintext[i]):
            ascii_num = ord(plaintext[i])
            out = ((((ascii_num-ord("A")) + ((ord(keyword[loop])-ord("a")))) % 26) + ord("A"))
            print(chr(out), end="")
            k+=1
            i+=1

        ## Check if plaintext is lower
        elif str.islower(plaintext[i]):
            ascii_num = ord(plaintext[i])
            out = ((((ascii_num-ord("a")) + ((ord(keyword[loop])-ord("a")))) % 26) + ord("a")) 
            print(chr(out), end="")
            k+=1
            i+=1
print("")
