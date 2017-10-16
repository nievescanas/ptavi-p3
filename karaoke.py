#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import json
import sys
from xml.sax import make_parser
import smallsmilhandler


class KaraokeLocal():

    def __init__(self):
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(sys.argv[1]))
        self.etiquetas = cHandler.get_tags()

    def __str__(self):
        objeto = ''
        for etiqueta in self.etiquetas:
            linea = str(etiqueta['name'])

            for atributo in etiqueta:
                if etiqueta[atributo] != etiqueta['name'] and etiqueta[atributo] != "":
                    linea += ('{tabulador}{atr}="{valor}"'.format(atr=atributo, valor=etiqueta[atributo], tabulador='\t'))
            objeto += ('{line}{salto}'.format(line=linea, salto='\n'))
        return(objeto)

    def do_json(self, name=''):
        if name == "":
            name = fich[:fich.find('.')]
            name = name + ".json"

        with open(name, 'w') as outfile:
            json.dump(self.etiquetas, outfile, separators=(',', ':'), indent="")

    def do_local(self):
        for dicc in self.etiquetas:
            if 'src' in dicc and 'http://' in dicc['src']:
                with urllib.request.urlopen(dicc['src']) as response:
                    name = dicc['src']
                    name = name[name.rfind('/')+1:]
                    urllib.request.urlretrieve(dicc['src'], filename=name)
                    dicc['src'] = name


if __name__ == "__main__":

    try:
        fich = sys.argv[1]
    except IndexError:
        sys.exit("Usage:python3 karaoke.py file.smil.")

    karaoke = KaraokeLocal()
    print(karaoke)
    karaoke.do_json()
    karaoke.do_local()

    karaoke.do_json('local.json')
    print(karaoke)
