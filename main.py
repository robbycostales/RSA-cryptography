#
# Author: Robert Costales
# Date: 2017 05 26
# Language: Python 3
# Purpose: Perform encryption and decryption of a piece of text using the RSA
#           method.

import crypto

# REF
# ord() converts character to corresponding ACII number
# chr() converts number to character

# contains original text
input_file = "inp.txt"
# where encrypted text will go
encrypt_file = "enc.txt"
# where decrypted text will go
decrypt_file = "dyc.txt"

# reads the input_file and encrypts it to the encrypt_file
#crypto.encrypt(input_file, encrypt_file)


j = crypto.phi(91)
print(crypto.EEA(5, j))
