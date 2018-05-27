#! /usr/bin/env python
# -*- coding: UTF-8; -*-

# app、modelsフォルダのどっちにも__init__.py格納しないとパッケージとして扱えないみたい・・・
from app.models.baby import Baby
from app.models.dog import Dog
from app.models.crow import Crow
from app.models.trainer import Trainer

def main():
    trainer = Trainer("トレーナー")

    # 各インスタンスを配列に格納
    animals = [Baby("つむぎ"), Dog("ぽち"), Crow("からすまる"), Trainer("たこあき")]
    for animal in animals:
        trainer.cry_animal(animal)


if __name__ == "__main__":
    main()
