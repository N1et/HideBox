# encoding: UTF-8
from Crypto.Cipher import AES
from PIL import Image
import stepic
import getpass
from PIL import Image
import sys
from std import *
def decryptdata(passw, dataF):
    lenpassw = len(passw)
    if lenpassw != 16 and lenpassw != 32:
        if lenpassw > 32:
            print_error("A senha deve ser no maximo 32 bytes")
            sys.exit()
        elif lenpassw < 16:
            null = 16-lenpassw
        else:
            null = 32-lenpassw
        passw+="\x00"*null

    digest, nonce, paycrypt = dataF[0:16], dataF[16:32], dataF[32:]
    key = AES.new(passw, AES.MODE_EAX, nonce)
    passw+=b"\x00"
    try:
        dataP = key.decrypt_and_verify(paycrypt, digest)
    except ValueError:
        print_error("Verificação de MAC falhou")
        sys.exit()
    return dataP

def encryptdata(passw, data):
    lenpassw = len(passw)
    if lenpassw != 16 and lenpassw != 32:
        if lenpassw > 32:
            print_error("A senha deve ser no maximo 32 bytes")
            sys.exit()
        elif lenpassw < 16:
            null = 16-lenpassw
        else:
            null = 32-lenpassw
        passw+="\x00"*null
    key = AES.new(passw, AES.MODE_EAX)
    paycrypt, digest = key.encrypt_and_digest(data)
    data = digest + key.nonce + paycrypt
    return data

def main_encrypt(data):
    print "AES - EAX. Max 32"
    passw = getpass.getpass("Password:")
    data = encryptdata(passw, data)
    return data

def main_decrypt(data):
    print "AES - EAX. Max 32 "
    passw = getpass.getpass()
    data = decryptdata(passw, data)
    return data
