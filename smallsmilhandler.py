#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        self.etiquetas = []    

    def startElement(self, name, attrs):
        dicc = {}
        if name == 'root-layout':
            dicc['Nombre'] = ('root-layout')
            dicc['width'] = attrs.get('width', "")
            dicc['height'] = attrs.get('height', "")
            dicc['background-color'] = attrs.get('background-color', "")
            self.etiquetas.append(dicc)
        elif name == 'region':
            dicc['Nombre'] = ('region')
            dicc['id'] = attrs.get('id', "")
            dicc['top'] = attrs.get('top', "")
            dicc['bottom'] = attrs.get('bottom', "")
            dicc['left'] = attrs.get('left', "")
            dicc['right'] = attrs.get('right', "")
            self.etiquetas.append(dicc)
        elif name == 'img':
            dicc['Nombre'] = ('img')
            dicc['src'] = attrs.get('src', "")
            dicc['region'] = attrs.get('region', "")
            dicc['begin'] = attrs.get('begin', "")
            dicc['dur'] = attrs.get('dur', "")
            self.etiquetas.append(dicc)
        elif name == 'audio':
            dicc['Nombre'] = ('audio')
            dicc['src'] = attrs.get('src', "")
            dicc['begin'] = attrs.get('begin', "")
            dicc['dur'] = attrs.get('dur', "")
            self.etiquetas.append(dicc)
        elif name == 'textstream':
            dicc['Nombre'] = ('textstream')
            dicc['src'] = attrs.get('src', "")
            dicc['region'] = attrs.get('region', "")
            self.etiquetas.append(dicc) 

    def get_tags(self):
        return self.etiquetas         

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())


