# -*- coding: utf-8 -*-
# @Time    : 2021
# @Author  : douzi
class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def speaking(self):
        print(f"{self.name}是一个{self.color}的小猫咪，今年{self.age}岁了，会讲话了")

    def running(self):
        print(f"{self.name}是一个小{self.gender},已经会跑了")


if __name__ == '__main__':
    animal = Animal("哈喽kitty", "粉色", 3, "母猫")
    animal.speaking()
    animal.running()
