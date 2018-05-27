#! /usr/bin/env python
# -*- coding: UTF-8; -*-

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    """
    抽象クラス
      衝突の可能性があるため、Javaと同じように1ファイル1クラスにしといたほうがよさげ
    """
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def cry(self):
        """
        抽象メソッド
          子クラスで、この関数がオーバーライドされてないとエラーとなる
        """
        pass
