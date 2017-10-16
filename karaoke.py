#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import json
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler  

class  ImpresionKaraoke(smallsmilhandler.SmallSMILHandler):

    def Url(self): 
        for dicc in self.etiquetas:
            if 'src' in dicc and 'http://' in dicc['src']:
                 with urllib.request.urlopen(dicc['src']) as response:
                    name = dicc['src']
                    name = name[name.rfind('/')+1:]
                    local_filename, headers = urllib.request.urlretrieve(dicc['src'],filename=name)
                    html = open(local_filename)
                    print (html)

    def WriteLine(self):
        for etiqueta in self.etiquetas:
            print ("{0:12}".format(etiqueta['name']), end="")

            for atributo in etiqueta:
                if etiqueta[atributo] != etiqueta['name'] and etiqueta[atributo] != "":
                    print(atributo,"=", "{0:12}".format(etiqueta[atributo]), end="")
            print("")
 
    def WritelineJson(self):
        with open('karaoke.json', 'w') as outfile:
            json.dump(self.etiquetas, outfile)


if __name__ == "__main__":
    
    parser = make_parser()
    cHandler = ImpresionKaraoke()
    parser.setContentHandler(cHandler)
    parser.parse(open(sys.argv[1]))
    cHandler.Url()
    cHandler.WriteLine()
    cHandler.WritelineJson()


