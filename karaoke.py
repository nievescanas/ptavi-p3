#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler  

class  ImpresionKaraoke(smallsmilhandler.SmallSMILHandler):

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
    cHandler.WriteLine()
    cHandler.WritelineJson()


