# -*- coding: utf-8 -*-
# @Time    : 2021
# @Author  : douzi
from python_Animal.Animal import Animal


class Cat(Animal):
    """
    继承父类Animal的speaking和running属性，定义一个新的属性hair
    """

    def __init__(self, name, color, age, gender, hair):
        super().__init__(name, color, age, gender)
        self.hair = hair

    def catching(self):
        print(f"{self.name}是一个{self.gender}，头顶着{self.hair},今年{self.age}岁了，会捉老鼠了")

    # 重写父类的方法
    def speaking(self):
        print("喵喵叫~")


if __name__ == '__main__':
    cat = Cat("银渐层", "银灰色", 3, "母猫", "短毛")
    cat.catching()
    cat.speaking()
