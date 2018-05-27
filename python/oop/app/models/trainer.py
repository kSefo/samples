#! /usr/bin/env python
# -*- coding: UTF-8; -*-

from app.abstract.animal import Animal

class Trainer(Animal):
    """
    トレーナー(Animalクラスを継承)
      動物を泣かすことができる
    """
    def __init__(self, name):
        super().__init__(name)
    
    def cry(self):
        return "おいらは、" + self.name

    def cry_animal(self, animal):
        """
        ポリモーフィズム(サブルーチンを呼び出す側のロジックを一本化する仕組み！！)
          どんな動物でも泣かせちゃう
        """
        print(animal.cry())
