import Keygen
import Crypt
import RSAInputParser


print("Welcome to Simple-RSA")

while True:
    print("\n*** Main Menue ***")
    print("(1) - Generate new keypairs")
    print("(2) - Encrypt message")
    print("(3) - Decrypt message")
    print("(0) - Exit")

    try:
        userIn = input("\nPlease choose operation: ")
        userIn = int(userIn)

    except KeyboardInterrupt:
        print("")
        break

    except ValueError:
        print("Please enter only Numbers between 0 and 4")
        continue

    if userIn == 1:
        keys = Keygen.keygen()

        print("*** Keypairs ***")
        print("- Private Key:   (N={},e={})".format(keys.private.RSA,
                                                    keys.private.exponent))
        print("- Public Key:    (N={},d={})".format(keys.public.RSA,
                                                    keys.public.exponent))

    elif userIn == 2 or userIn == 3:
        Key = RSAInputParser.InputParser(input("Please enter RSA-Key: "))

        if userIn == 2:
            message = input("Please enter the plaintext message: ")
            encrypted = Crypt.encrypt(Key.N, Key.exp, message)
            print("Encrypted: {}".format(encrypted))
        else:
            message = input("Please enter the encrypted message: ")
            decrypted = Crypt.decrypt(Key.N, Key.exp, message)
            print("Dcrypted: {}".format(decrypted))

    elif userIn == 0:
        break

print("Bye Bye")
