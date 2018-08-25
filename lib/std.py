import sys

def print_error(text):
    simbol = "ERROR:"+" "
    print >> sys.stderr, simbol+str(text)

def print_status(text):
    simbol = "[i]"+" "
    print >> sys.stdout, simbol+str(text)

    
