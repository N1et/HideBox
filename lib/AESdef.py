# encoding: UTF-8
from Crypto.Cipher import AES
from PIL import Image
import stepic
import getpass
from PIL import Image
import sys

def decryptdata(passw, dataF):
        if len(passw) > 32:
            print >> sys.stderr, "ERROR: a senha deve ser no maximo 32 bytes"
            sys.exit()
        digest, nonce, paycrypt = dataF[0:16], dataF[16:32], dataF[32:] 
        while 1:
                try:
                        key = AES.new(passw, AES.MODE_EAX, nonce)
                        break
                except ValueError:
                        passw+=b"\x00"
        try:
                dataP = key.decrypt_and_verify(paycrypt, digest)
        except:
                print >> sys.stderr, "ERROR: Senha incorreta."
                sys.exit()
        return dataP

def encryptdata(passw, file1, filename):
    if len(passw) > 32:
        print >> sys.stderr, "ERROR: senha deve ser no maximo 32 bytes"
        sys.exit()

    while 1:
        try:
            key = AES.new(passw, AES.MODE_EAX)
            break
        except:
            passw+=b"\x00"
    fileO = open(file1, 'r')
    paycrypt, digest = key.encrypt_and_digest(fileO.read())
    fileO.close()
    data = digest + key.nonce + paycrypt
    return data
def main_encrypt(image, file1, fileout):
    if fileout is None:
        fileout = image + ".hd"
    image = Image.open(image)
    stepic._validate_image(image)
    print "AES - EAX. Max 32"
    passw = getpass.getpass("Password:")
    data = encryptdata(passw, file1, fileout)
    stepic.encode_inplace(image, data)
    image.save(fileout, image.format)
def main_decrypt(image, fileout):
        try:
                imageO = Image.open(image)
        except IOError:
                print >> sys.stderr, image+": Imagem não encontrada"
                sys.exit()
        stepic._validate_image(imageO)
        data = stepic.decode(imageO)

	print "AES - EAX. Max 32 "
	passw = getpass.getpass()
	if len(data) < 16:
		print >> sys.stderr, image+": Não foi encontrado nenhum dado na imagem"
		sys.exit()
	data = decryptdata(passw, data)
	if fileout is None:
		print "------------BEGIN-----------"
		print data
		print "------------END-------------"
	else:
		fileo = open(fileout, 'wb')
		fileo.write(data)
		fileo.close()
		print "Salvo em", fileout
