# Using public key cryptography is like signing a message with 
# your own digital signature. Not only does it prevent 
# unauthorised people from reading your message, it proves that 
# the message originates from the person who claims to have sent 
# it.
#
# The public key can be any number which meets the following 
# criteria:
#     * It is chosen using a random source of information so that 
#       it is unpredictable.
#     * It is the product of two numbers, A * B = AB, and A and 
#       B are both prime numbers (each only divisible by itself 
#       and 1).
#     * This product AB is a large number and therefore has many 
#       digits.
#     * A and B are used as private keys and are the only factors 
#       of the public key AB.
#
# We can see how this works in practice as follows:
# Suppose we ignore the requirement for the public key to be a 
# large number for now and use small randomly chosen prime numbers, 
# A=2 and B=5. This makes the public key AB = 2 * 5 = 10. It is 
# easy to work out that A=2 and B=5 are the only possible factors 
# of 10.
#
# If we use A=2 and B=5 as the private keys, AB = 10 becomes the 
# public key. Let’s assume Alice uses A=2 as her private key and 
# Bob uses B=5 as his.
# 
# Now imagine an attacker intercepts the message sent from Bob to 
# Alice. The attacker can find out that the public key was 10 
# because it will need to be sent along with the encrypted message, 
# and the attacker may even know that the private keys are the 
# factors of the public key.
#
# So from the attacker’s point of view, to break the cryptography 
# they will need to find A and B by finding the factors of the public 
# key, AB = 10
#
# Because we have chosen small value private keys, A=2 and B=5, 
# in this example, it is very easy for the attacker to figure out 
# what these private keys are. All they have to do is multiply all 
# possible values of A and B and see which multiplication results 
# in the value 10. In this example, the attacker could probably 
# even do it in their head!
# 
# However, if the public key were a larger number, it would be 
# considerably more difficult to work out the factors. Essentially, 
# this is what protects the message: a hard maths problem.


#
# Caesar cipher - a shift of the letters of the alphabet with
#                 wrap-around at the end for continuity
#
def caesar( plaintext, cipherkey ):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    ciphertext = ""

    # shift each letter in the plain text by the value of 'cipherkey'
    for i in range(len(plaintext)):
        idx = alphabet.index(plaintext[i])

        # wrap around at top on encrypt
        idx =  (idx + cipherkey) % len(alphabet) 

        # prevent underflow on decrpt
        if (idx<0): idx += len(alphabet)

        # apply shift to the character        
        ciphertext = ciphertext + alphabet[idx]

    return( ciphertext )


