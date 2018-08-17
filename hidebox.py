#! /usr/bin/python2
# encoding: UTF-8
import sys
sys.path.append("lib/")
from AESdef  import *
from PIL import Image
import getpass
import base64
import stepic
import optparse



parser = optparse.OptionParser(usage="%prog [-e] -i IMAGE -f FILE", 
        version="HideBox 0.1",
        description="HideBox - Oculta arquivos em imagens de forma segura.")
parser.add_option("-e", "--encode", action="store_true", default=False,
        help = "Modo de criptografar e codificar dado na imagem apontada.")
parser.add_option("-d", "--decode", action="store_true", default=False,
        help = "Modo de descriptografar e decodificar o dado na imagem apontada")
parser.add_option("-i", action="store", dest="IMAGE", 
        help = "IMAGE alvo que recebera o FILE")
parser.add_option("-f", "--file", action="store", dest="FILE",
        help = "FILE alvo que sera codificado na IMAGE.")
parser.add_option("-o", "--out", action="store", metavar='FILE', dest="FILEOUT", 
        help = "Escreve os dados obtidos de IMAGE no arquivo FILELEOUT.")

opt, args = parser.parse_args()
if len(sys.argv) == 1:
    parser.print_usage()
    print "\"-h\" for more information"
    sys.exit(2)
if opt.encode == opt.decode:
    parser.print_usage()
    print >> sys.stderr, "Escolha entre -e para codificar, -d para decodificar"
    sys.exit()
elif opt.IMAGE is None:
	parser.print_usage()
	print >> sys.stderr, "ERROR: \"-i\" é necessário"
	sys.exit()
try:
    if opt.decode:
            main_decrypt(opt.IMAGE, opt.FILEOUT)
    elif opt.encode:
            main_encrypt(opt.IMAGE, opt.FILE, opt.FILEOUT)
except KeyboardInterrupt:
    print "Operação Cancelada"
    pass

