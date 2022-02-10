# -*- coding: utf-8 -*-

print("#####################  é \"cp1252\"  ###########################")
print ( "é".encode("cp1252") )           
print ( list ("é".encode("cp1252"))  ) 

print (b'\xe9\xe9'.decode("cp1252"))

print("#####################  € \"cp1252\"  ###########################")
ch="€"
print (ch.encode("cp1252") )           
print ( list (ch.encode("cp1252"))  ) 

octet = b'\x80'
print (octet.decode("cp1252"))

print("#####################  € \"iso8859-15\"  ###########################")
print ( "€".encode("iso8859-15") )           
print ( list ("€".encode("iso8859-15"))  ) 

octets = b'\xa4\xa4\xa4'
print (octets.decode("iso8859-15"))

print("#####################  € \"utf8\"  ###########################")

print ( "€".encode("utf8") )           
print ( list ("€".encode("utf8"))  ) 

print (b'\xe2\x82\xac'.decode("utf8"))

# remarque : si on essaie de décoder la suite de 3 octets avec un autre système
print (b'\xe2\x82\xac'.decode("iso8859-15"))


print("#####################  chr / ord  ###########################")

print(chr(65))
print(ord('A'))

print(chr(50))
print(ord('2'))

print(chr(233))
print(ord('é'))

print(chr(8364))
print(ord('€'))

import sys
print(sys.stdout.encoding)