#! /usr/bin/python2
# encoding: UTF-8
import sys
sys.path.append("lib/")


from PIL import Image
import getpass
import optparse
import os
import stepic
from std import *

cryptoptions = ["AES"] #Criptografias disponiveis.
#   Para implementar uma nova criptografia, é necessário adicionar o nome do arquivo aqui
#   é preciso que o lib/arquivodef.py tenha duas funções main_encrypt e main_decrypt
#   e tenha o nome "def" no final do nome

parser = optparse.OptionParser(usage="%prog [-e] -i IMAGE -f FILE",
        version="HideBox 0.0.10",
        description="HideBox - Oculta arquivos em imagens de forma segura.")
parser.add_option("-e", "--encode", action="store_true", default=False,
        help = "Modo de criptografar e codificar dado na imagem apontada.")
parser.add_option("-d", "--decode", action="store_true", default=False,
        help = "Modo de descriptografar e decodificar o dado na imagem apontada")
parser.add_option("-i", action="store", dest="IMAGE",
        help = "IMAGE alvo que recebera o FILE")
parser.add_option("-f", action="store", dest="FILE",
        help = "FILE alvo que sera codificado na IMAGE.")
parser.add_option("-c", action="store", dest="CRYPT", default="AES",
        help = "criptografia que sera usada")
parser.add_option("--list-crypt",  action="store_true", dest="list_crypt",
        help = "criptografia que sera usada")
parser.add_option("-o", "--out", action="store", metavar='FILE', dest="FILEOUT",
        help = "Escreve os dados obtidos de IMAGE no arquivo FILEOUT.")

opt, args = parser.parse_args()

#verificações de argumentos
if opt.list_crypt:
    print ' - '.join(cryptoptions)
    sys.exit()

if len(sys.argv) == 1 or opt.decode == opt.encode or not opt.IMAGE:
    parser.print_usage()
    sys.exit()
if opt.encode and not opt.FILE:
    parser.print_usage()
    sys.exit()

# verificando se os arquivos passados estão disponiveis
if not os.path.isfile(opt.IMAGE):
    print_error("A imagem não foi encontrada")
    sys.exit()
elif opt.FILE:
    if not os.path.isfile(opt.FILE):
        print_error("O Arquivo não foi encontrado")
        sys.exit()

if not opt.CRYPT in cryptoptions:
    print_error("A criptografia escolhida não está disponível")
    sys.exit()
#importando o modulo solicitado, sempre será nomeado de "crypt"
else:
    modulename = opt.CRYPT+"def" # [modulename]def.py
    globals()["crypt"] = __import__(modulename)

imagem = opt.IMAGE
file_in = opt.FILE
file_out = opt.FILEOUT

#main
image_obj = Image.open(imagem)
stepic._validate_image(image_obj)
if opt.encode:
    if not file_out:
        file_out = "%s.hd" %(imagem)
    data = open(file_in, "r").read()
    data = crypt.main_encrypt(data)
    stepic.encode_inplace(image_obj, data)
    image_obj.save(file_out, image_obj.format) 

elif opt.decode:
    data = stepic.decode(image_obj)
    data = crypt.main_decrypt(data)
    if not file_out:
        print "------------BEGIN-----------\n", data, "------------END-------------"
    else:
        fileo=open(opt.FILEOUT, "w")
        fileo.write(data)
        fileo.close()
else:
    parser.print_usage()
image_obj.close()
