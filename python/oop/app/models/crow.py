#! /usr/bin/env python
# -*- coding: UTF-8; -*-

from app.abstract.animal import Animal

class Crow(Animal):
    """
    カラス(Animalクラスを継承)
    """
    def __init__(self, name):
        super().__init__(name)
    
    def cry(self):
        return "カー"
