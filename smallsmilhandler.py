#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.etiquetas = []
        self.dicc = {
            'root-layout': ['width', 'height', 'background-color'],
            'region': ['id', 'top', 'bottom', 'left', 'right'],
            'img': ['src', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'begin', 'dur']}

    def startElement(self, name, attrs):
        dicc = {}
        if name in self.dicc:
            dicc['name'] = name
            for atributo in self.dicc[name]:
                    dicc[atributo] = attrs.get(atributo, "")
            self.etiquetas.append(dicc)

    def get_tags(self):
        return self.etiquetas

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open())