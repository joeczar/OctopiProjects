# This code implements the Caesar cipher, but using public key
# encryption techniques. No one would actually do this, but as
# the Caesar cipher is easy to understand, it's a potentially
# handy cipher technique in order to explain PKC.
#
# Instead of passing the key (amount of shift) privately through
# an independent channel, we can pass the public key with the 
# message. 

# All original code: Crown Copyright 2017 

from caesar import caesar

# public key is the product of two private keys which are prime numbers
privatekey = [ [ 2, 5 ], [ 7, 11 ], [ 13, 17 ], [ 19, 23 ] ]


# Encrypting or decrypting?
encrypt = input( "Encrypting or decrypting (E or D)? ")
encrypt = encrypt.upper() #  convert to upper case
if (encrypt == "E"):
    encrypting = True
elif (encrypt == "D"):
    encrypting = False
else:
    print( "must be E or D, cannot continue" )
    exit(0)

# Which set of keys should be used
print("Choice of keys is as follows:")
for i in range(len(privatekey)):
    print( "Private key set %s is [ %s, %s ] (public key %s)" % (i, privatekey[i][0], privatekey[i][1], privatekey[i][0] * privatekey[i][1]))
keyindex = int( input("Which set of keys? (0-3) ") )
if (keyindex > 3):
    print( "Keys must be in range (0-3), cannot continue" )
    exit(0)

# find out if private key A or B should be used
user = input( "Which user - Alice or Bob (A or B)? ")
user = user.upper() #  convert to upper case
if (user == "A"):
    username = "Alice"
    # Alice's private key choice from the selected set depends on whether she is encrypting or decrypting  
    if (encrypting): 
        useridx = 0 
    else: 
        useridx = 1
elif (user == "B"):
    # Bob's private key choice from the selected set depends on whether he is encrypting or decrypting  
    username = "Bob"
    if (encrypting): 
        useridx = 1 
    else: 
        useridx = 0
else:
    print( "User must be A or B, cannot continue" )
    exit(0)

# what plain text should be enciphered
msgtext = input( "Message text to be processed using Caesar cipher? ")
msgtext = msgtext.replace(" ", "X") # replace space with 'X'
msgtext = msgtext.upper()           # force all characters to upper case

# public key is the product of the pair of private keys 
publickey = privatekey[keyindex][0] * privatekey[keyindex][1]

# explain what we are doing
print( "Public key is %s for set %s, so private key to be used by %s is %s" % (publickey, keyindex, username, privatekey[keyindex][useridx]) )

# obtain the caesar cipher using the selected private key 
if (encrypting):
    ciphertext = caesar(msgtext, privatekey[keyindex][useridx] )
else:
    plaintext = caesar(msgtext, -privatekey[keyindex][useridx] )

if (encrypting):
    print( "%s therefore sends public key %s and %s as cipher text %s" % (username, publickey, msgtext, ciphertext) )
else:
    print( "%s therefore decrypts %s as %s" % (username, msgtext, plaintext) )

