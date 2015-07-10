from binascii import hexlify


def encrypt(RSA, exponent, plaintext):

    cipperText = str()

    # Character by character
    for index in range(len(plaintext)):
        plainChar = plaintext[index]

        # ascii = ord(plainChar)
        plainChar = int(hexlify(plainChar.encode()), 16)
        cipperChar = plainChar ** exponent % RSA

        cipperText = "{}:{}".format(cipperText, hex(cipperChar)[2:])

    return cipperText[1:]


def decrypt(RSA, exponent, cippertext):

    plainText = str()
    cipper = cippertext.split(":")

    # Character by character
    for cipperChar in cipper:
        plainChar = int(cipperChar, 16) ** exponent % RSA
        plainChar = chr(plainChar)

        plainText = "{}{}".format(plainText, plainChar)

    return plainText
